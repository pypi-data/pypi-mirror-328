#! /usr/bin/env python3
from __future__ import absolute_import, print_function, division, unicode_literals
try:
    from future_builtins import zip, map # Use Python 3 "lazy" zip, map
except ImportError:
    pass

import ast
import errno
import logging
import multiprocessing
import os
import re
import socket
import sys
import time
import threading
import traceback

import pytest

if __name__ == "__main__":
    # Ensure we always use *this* cpppo Python module during tests, if we're run by a Python interpreter!
    if __package__ is None:
        __package__	= "cpppo.server.enip"
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    from cpppo.automata import log_cfg
    log_cfg['level']	= logging.NORMAL
    logging.basicConfig( **log_cfg )


from cpppo.dotdict import dotdict, apidict
from cpppo.misc import timer, near
from cpppo.modbus_test import start_simulator
from cpppo.server import enip, network
from cpppo.server.enip import poll, ucmm
from cpppo.server.enip.main import main as enip_main
from cpppo.server.enip.ab import powerflex, powerflex_750_series
from cpppo.server.enip.get_attribute import proxy

    
def start_powerflex_simulator( *options ):
    return start_simulator(
        os.path.abspath( __file__ ), '-a', 'localhost:0', '-A', '-p', '--no-udp', '-v',
        *options
    )


@pytest.fixture( scope="module" )
def simulated_powerflex_gateway( request ):
    command,address		= start_powerflex_simulator( 'SCADA=INT[100]' )
    request.addfinalizer( command.kill )
    return command,address


def test_powerflex_simple( simulated_powerflex_gateway ):
    command,address             = simulated_powerflex_gateway
    try:
        assert address, "Unable to detect PowerFlex EtherNet/IP CIP Gateway IP address"
        pf			= powerflex( host=address[0], port=address[1], timeout=1 )

        # Reading a list of nothing should work...
        assert list( pf.read( [] )) == []
        # At the least, it ensures we have a non-None .identity
        print( "PowerFlex Identity: %s" % pf )
        assert "None" not in str( pf ), "No EtherNet/IP CIP connection, or no Identity"

        # Simple read of Tag, using Read Tag; returns list of bare list of data elements
        tag			= "SCADA[0-9]"
        value,			= pf.read( [ tag ] )
        print( "Tag:            %15s: %r" % ( tag, value ))
        assert type( value ) is list and all( v == 0 for v in value )

        # Read of CIP Object/Instance/Attribute using Get Attribute Single, interpreted as an
        # arbitrary CIP data type.  Returns list of result values, each a dict of decoded data.
        # Providing a type to use to decode the data produces whatever dictionary the type parses
        # into, unchanged:
        get			= ( "@1/1/1", enip.INT )
        value,			= pf.read( [ get ] )
        print( "Vendor Number:  %15s: %r" % ( get[0], value ))
        assert len( value ) == 1 and 'INT' in value[0] and value[0]['INT'] == 0x0001

        get			= ( "@1/1/7", enip.SSTRING )
        value,			= pf.read( [ get] )
        print( "Product Name:   %15s: %r" % ( get[0], value ))
        assert len( value ) == 1 and 'SSTRING' in value[0] and value[0].SSTRING.string == 'PowerFlex/20-COMM-E'

        # Get the DPI Parameter 0x93, Instance 3, Attribute 9 Output_Current attribute, interpreted
        # as REAL.  1 element.
        get			= ( "@0x93/7/10", enip.REAL )
        value,			= pf.read( [ get] )
        print( "Output_Current: %15s: %r" % ( get[0], value ))
        assert len( value ) == 1 and 'REAL' in value[0] and near( value[0].REAL, 123.45 )

        # Get the DPI parameter 0x93, Instance 3, Attribute 9 Output_Current attribute, interpreted
        # as INT.  1 element.  Providing named CIP types shucks the dictionary container, and
        # produces just the target typed data:
        get			= ( "@0x93/140/10", "INT" )
        value,			= pf.read( [ get] )
        print( "Accel_Time_1:   %15s: %r" % ( get[0], value ))
        assert len( value ) == 1 and value[0] == 567
        get			= ( "@1/1", [ "INT", "INT", "INT", "INT", "INT", "DINT", "SSTRING", "USINT" ])
        value,			= pf.read( [ get] )
        print( "Identity (all): %15s: %r" % ( get[0], value ))
        assert value == [1, 14, 54, 2836, 12640, 7079450, u'PowerFlex/20-COMM-E', 255]

        # TCPIP Object
        get			= ( "@0xF5/1", [
            "DWORD", "DWORD", "DWORD", "EPATH",
            "IPADDR", "IPADDR", "IPADDR", "IPADDR", "IPADDR", "STRING",
            "STRING"
            ])
        value,			= pf.read( [ get] )
        print( "TCPIP (all):    %15s: %r" % ( get[0], value ))
        assert value == [2, 48, 16, [{'class': 246}, {'instance': 1}], '10.0.0.4', '255.255.252.0', '10.0.0.1', '10.0.0.1', '8.8.8.8', u'example.com', u'powerflex']
        
        # List Identity
        ident			= pf.list_identity()
        assert ident.sin_addr == "10.0.0.4"

    except Exception as exc:
        logging.warning( "Test terminated with exception: %s", exc )
        raise


def test_powerflex_poll_success( simulated_powerflex_gateway ):
    command,address             = simulated_powerflex_gateway
    try:
        assert address, "Unable to detect PowerFlex EtherNet/IP CIP Gateway IP address"
        values			= {}
        def process( p, v ):
            print( "%s: %16s == %s" % ( time.ctime(), p, v ))
            values[p]		= v    
        process.done		= False

        params			= [ 'Output Current', 'Motor Velocity', 'Speed Units' ]

        poller			= threading.Thread(
            target=poll.poll, args=(powerflex_750_series,), kwargs={ 
                'address': 	address,
                'cycle':	1.0,
                'timeout':	0.5,
                'params':	params,
                'process':	process,
            })
        poller.deamon		= True
        poller.start()

        try:
            # Polling starts immediately
            time.sleep(.5)
            assert len( values ) == len( params )

            # Make sure it repeats
            values.clear()
            assert len( values ) == 0
            time.sleep(1.0)
            assert len( values ) == len( params )

            # Allow time to refresh values on next poll
            values['Output Current'] = 1.0
            time.sleep(1.0)
        finally:
            process.done	= True

        poller.join( 1.0 )
        assert not poller.is_alive(), "Poller Thread failed to terminate"
    
        assert 'Output Current' in values and near( values['Output Current'][0], 123.45 )
        assert 'Motor Velocity' in values and near( values['Motor Velocity'][0], 789.01 )

    except Exception as exc:
        logging.warning( "Test terminated with exception: %s", exc )
        raise


def test_powerflex_poll_failure():
    """No PowerFlex simulator alive; should see exponential back-off.  Test that the poll.poll API can
    withstand gateway failures, and robustly continue polling.

    """
    #logging.getLogger().setLevel( logging.INFO )
    def null_server( conn, addr, server=None ):
        """Fake up an EtherNet/IP server that just sends a canned EtherNet/IP CIP Register and Identity
        string response, to fake the poll client into sending a poll request into a closed socket.
        Immediately does a shutdown of the incoming half of the socket, and then closes the
        connection after sending the fake replies, usually resulting in an excellent EPIPE/SIGPIPE
        on the client.  Use port 44819, to avoid interference by (possibly slow-to-exit) simulators
        running on port 44818.

        """
        logging.normal( "null_server on %s starting" % ( addr, ))
        conn.shutdown( socket.SHUT_RD )
        time.sleep( 0.1 )
        conn.send( b'e\x00\x04\x00\xc9wH\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00' )
        conn.send( b'c\x00;\x00\xd4/\x9dm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0c\x005\x00\x01\x00\x00\x02\xaf\x12\n\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0e\x006\x00\x14\x0b`1\x1a\x06l\x00\x13PowerFlex/20-COMM-E\xff' )
        conn.close()
        while server and not server.control.done:
            time.sleep( .1 )
        logging.normal( "null_server on %s done" % ( addr, ))

    try:
        values			= {} # { <parameter>: <value> }
        failed			= {} # { <time>: <exc> }

        control			= dotdict()
        control['done']		= False

        for _ in range( 3 ):
            server		= threading.Thread(
                target=network.server_main, kwargs={
                    'address': 	('localhost',44819),
                    'target':	null_server,
                    'kwargs': {
                        'server': dotdict({
                            'control': control
                        })
                    },
                    'udp':	False, # no UDP server in this test
                })
            server.daemon		= True
            server.start()
            time.sleep(.5)
            if server.is_alive:
                break
        assert server.is_alive, "Unable to start null_server on localhost"

        def process( p, v ):
            logging.normal( "process: %16s == %s", p, v )
            values[p]		= v
        process.done		= False

        def failure( exc ):
            logging.normal( "failed: %s", exc )
            elapsed		= int(( timer() - failure.start ) * 1000 ) # ms.
            failed[elapsed]	= str( exc )
        failure.start		= timer()
    
        params			= [ 'Output Current', 'Motor Velocity', 'Speed Units' ]

        backoff_min		= 0.5
        backoff_max		= 4.0
        backoff_multiplier	= 2.0 # --> backoff == .5, 1.0, 2.0, 4.0
        poller			= threading.Thread(
            target=poll.poll, kwargs={ 
                'proxy_class':	powerflex_750_series,
                'address': 	('localhost',44819),
                'cycle':	1.0,
                'timeout':	0.5,
                'backoff_min':	backoff_min,
                'backoff_max':	backoff_max,
                'backoff_multiplier': backoff_multiplier,
                'params':	params,
                'process':	process,
                'failure':	failure,
            })
        poller.deamon		= True
        poller.start()

        try:
            # Polling starts immediately, but the first poll occurs after an attempt to get the
            # Identity string, hence two timeouts for the first poll failure.
            while len( failed ) < 3 and timer() - failure.start < 10.0:
                time.sleep(.1)
        finally:
            process.done	= True
            control.done	= True
        poller.join( backoff_max + 1.0 ) # allow for backoff_max before loop check
        assert not poller.is_alive(), "Poller Thread failed to terminate"
        server.join( 1.0 )
        assert not server.is_alive(), "Server Thread failed to terminate"

        # Check that each failure is (at least) the expected backoff from the last
        assert len( failed ) > 0
        k_last			= None
        backoff			= backoff_min
        for k in sorted( failed ):
            logging.normal( "Poll failure at %4dms (next backoff: %7.3fs): %s", k, backoff, failed[k] )
            if k_last is not None:
                assert k - k_last >= backoff
            backoff		= min( backoff_max, backoff * backoff_multiplier )
            k_last		= k

        assert len( values ) == 0

    except Exception as exc:
        logging.warning( "Test terminated with exception: %s", exc )
        raise



class powerflex_routed( proxy ):
    PARAMETERS			= powerflex_750_series.PARAMETERS


def powerflex_routed_cli( number, address=None ):
    with powerflex_routed( host=address[0], port=address[1], route_path="1/1" ) as via:
        (freq,), = via.read( via.parameter_substitution( 'Output Frequency' ))
        logging.normal( "Output Frequency == {}".format( freq ))
        (velo,), = via.read( via.parameter_substitution( 'Motor Velocity' ))
        logging.normal( "Motor Velocity == {}".format( velo ))

    # .bench client_funcs return Falsey on Success
    return not ( near( freq, 456.78 ) and near( velo, 789.01 ))


@pytest.mark.xfail # unreliable; unknown...
def test_powerflex_poll_routing_bench( simulated_powerflex_gateway ):
    command,address             = simulated_powerflex_gateway

    class UCMM_routing_to_powerflex( ucmm.UCMM ):
        route			= {
            "1/1": "{}:{}".format( *address ),
        }

    with multiprocessing.Manager() as m:
        server_kwds		= dict(
            argv	= [
                "-v", "--address", "localhost:0", '-A', '--no-udp',
            ],
            UCMM_class	= UCMM_routing_to_powerflex,
            server	= dotdict(
                control	= m.apidict(
                    timeout	= 1.0,
                    done	= False
                )
            ),
        )

        failed			= network.bench(
            server_func	= enip_main,
            server_kwds	= server_kwds,
            client_func	= powerflex_routed_cli,
            client_kwds	= None,
            client_count= 1,
            client_max	= 1,
            address_delay= 5.0,
        )
    assert not failed, \
        "Failed Powerflex poll routing via network.bench"

'''
# 
# NOT RELIABLE.
# 
def test_powerflex_poll_routing( simulated_powerflex_gateway ):
    """Test all the various proxy class for routing a request to the powerflex.  Sets up a simulated
    C*Logix PLC with a gateway to the simulated Powerflex."""
    command,address             = simulated_powerflex_gateway

    # We *must* have the simulated C*Logix on localhost:44818, because some proxy classes cannot be
    # configured to use any other port than the default EtherNet/IP port.

    class UCMM_routing_to_powerflex( ucmm.UCMM ):
        route			= {
            "1/1": "{}:{}".format( *address ),
        }
    
    control			= apidict( timeout=1.0 )
    control['done']		= False
    for _ in range( 3 ):
        clogix		= threading.Thread(
            target=enip_main,
            args		= (
                [ "-v", "--address", "localhost:44818" ],
            ),
            kwargs		= dict(
                UCMM_class	= UCMM_routing_to_powerflex,
                server		= dotdict(
                    control	= control
                ),
                udp		= False, # no UDP server in this test
            ))
        clogix.daemon		= True
        clogix.start()
        time.sleep(.5)
        if clogix.is_alive:
            break
    assert clogix.is_alive, "Unable to start C*Logix on localhost:44818"

    class powerflex_routed( proxy ):
        PARAMETERS		= powerflex_750_series.PARAMETERS
    try:
        with powerflex_routed( host=address[0], route_path="1/1" ) as via:
            (freq,), = via.read( via.parameter_substitution( 'Output Frequency' ))
            logging.normal( "Output Frequency == {}".format( freq ))
        assert near( freq, 456.78 )
    finally:
        control.done		= True
'''
    
# 
# python poll_test.py -- AB PowerFlex simulator for testing
# 

class UCMM_no_route_path( ucmm.UCMM ):
    """The PowerFlex/20-COMM-E UnConnected Messages Manager allows no route_path"""
    route_path			= False


class DPI_Parameters( enip.Object ):
    """Each Instance corresponds to a PowerFlex parameter.  Writing to Attribute 9 updates the EEPROM in
    the device, while writing to Attribute 10 (0xA) updates only the (temporary) RAM memory in the
    PowerFlex.  Therefore, we'll set both Attribute 9/10 to point to the same simulated Attribute.
    
    TODO:

    Parameter Object 0x0F is supported in the PowerFlex 7-Class Drivers, but not in the
    750-Series. DPI Parameter Object 0x93 is supported in both (with restriction); see
    http://literature.rockwellautomation.com/idc/groups/literature/documents/um/20comm-um010_-en-p.pdf,
    Chapter 6-2.

    For this simulation, we'll make the DPI Parameter Object 0x93 Instances, Attributes 9 and 10
    (0x0A) all point to the same Attribute object, and reading/writing these Attributes at any of
    their addresses will all access the same Attribute data.

    """
    class_id			= 0x93

    # Simulated PowerFlex Parameters; correspond to DPI Object's Instance numbers
    OUTPUT_FREQ			= 1
    MTR_VEL_FDBK		= 3
    OUTPUT_CURRENT		= 7
    DC_BUS_VOLTS		= 11
    ELAPSED_KWH			= 14
    ACCEL_TIME_1		= 140
    SPEED_UNITS			= 300
    def __init__( self, name=None, **kwds ):
        super( DPI_Parameters, self ).__init__( name=name, **kwds )
        if self.instance_id == 0:
            # Extra Class-level Attributes
            pass
        elif self.instance_id == self.OUTPUT_FREQ:
            self.attribute[ '9']= \
            self.attribute['10']= enip.Attribute( 'Output_Freq',	enip.REAL, default=456.78 )
        elif self.instance_id == self.MTR_VEL_FDBK:
            self.attribute[ '9']= \
            self.attribute['10']= enip.Attribute( 'Mtr_Vel_Fdbk',	enip.REAL, default=789.01 )
        elif self.instance_id == self.OUTPUT_CURRENT:
            self.attribute[ '9']= \
            self.attribute['10']= enip.Attribute( 'Output_Current',	enip.REAL, default=123.45 )
        elif self.instance_id == self.DC_BUS_VOLTS:
            self.attribute[ '9']= \
            self.attribute['10']= enip.Attribute( 'DC_Bus_Volts',	enip.REAL, default=0.08 )
        elif self.instance_id == self.ELAPSED_KWH:
            self.attribute[ '9']= \
            self.attribute['10']= enip.Attribute( 'Elapsed_KwH',	enip.REAL, default=987.65 )
        elif self.instance_id == self.ACCEL_TIME_1:
            self.attribute[ '9']= \
            self.attribute['10']= enip.Attribute( 'Accel_Time_1',	enip.INT, default=567 )
        elif self.instance_id == self.SPEED_UNITS:
            self.attribute[ '9']= \
            self.attribute['10']= enip.Attribute( 'Speed_Units',	enip.DINT, default=1 ) # RPM
        else:
            raise AssertionError( "Unrecognized PowerFlex Parameter / Instance ID: %s" % ( self.instance_id ))

        # TODO: Set up all appropriate instance attributes here, as per self.instance_id


def main( **kwds ):
    """Set up PowerFlex/20-COMM-E objects (enip.main will set up other Logix-like objects)"""

    enip.config_files 	       += [ __file__.replace( '.py', '.cfg' ) ]

    DPI_Parameters( name="DPI_Parameters", instance_id=0 ) # Class Object
    DPI_Parameters( name="DPI_Parameters", instance_id=DPI_Parameters.OUTPUT_FREQ )
    DPI_Parameters( name="DPI_Parameters", instance_id=DPI_Parameters.MTR_VEL_FDBK )
    DPI_Parameters( name="DPI_Parameters", instance_id=DPI_Parameters.OUTPUT_CURRENT )
    DPI_Parameters( name="DPI_Parameters", instance_id=DPI_Parameters.DC_BUS_VOLTS )
    DPI_Parameters( name="DPI_Parameters", instance_id=DPI_Parameters.ELAPSED_KWH )
    DPI_Parameters( name="DPI_Parameters", instance_id=DPI_Parameters.ACCEL_TIME_1 )
    DPI_Parameters( name="DPI_Parameters", instance_id=DPI_Parameters.SPEED_UNITS )

    # Establish Identity and TCPIP objects w/ some custom data for the test, from a config file
    return enip_main( argv=sys.argv[1:], UCMM_class=UCMM_no_route_path )



if __name__ == "__main__":
    sys.exit( main() )
