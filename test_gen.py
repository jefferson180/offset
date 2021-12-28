from  general  import  *
import  unittest

class  TestComputer ( unittest . TestCase ):
    "" "Test: computer address" ""
    def  test_ip ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        result  =  comp . get_interface (). address
        self . assertEqual ( result , "172.10.10.1" )

    "" "Test: computer name" ""
    def  test_name ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        result  =  comp . name
        self . assertEqual ( result , "First" )

    "" "Test: ping without network" ""
    def  test_ping_without_net ( self ):
        comp  =  Computer ( "First" )
        result  =  comp . ping ( "172.10.10.10" )
        self . assertEqual ( result , "No network" )

    "" "Test: ping" ""
    def  test_ping ( self ):
        comp1  =  Computer ( "First" )
        comp2  =  Computer ( "Second" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        net . add_host ( comp2 , "172.10.10.2" )
        result  =  comp1 . ping ( "172.10.10.2" )
        self . assertEqual ( result , "Success ping from 172.10.10.1 to 172.10.10.2" )

    "" "Test: Get the computer name" ""
    def  comp_get_name ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        addr  =  "1.2.3.4"
        net . add_host ( comp , addr )
        result  =  net . hosts [ addr ]. get_name ()
        self . assertEqual ( result , "First" )

    "" "Test: resolving the name of a non-existent computer" ""
    def  test_comp_resolve_unk_name ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        result  =  comp . local_resolve ( "172.10.10.2" )
        self . assertEqual ( result , "Unknown host" )

    "" "Test: Resolve Computer Name" ""
    def  test_comp_name_resolve ( self ):
        comp1  =  Computer ( "First" )
        comp2  =  Computer ( "Second" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        net . add_host ( comp2 , "172.10.10.2" )
        result  =  comp1 . local_resolve ( "172.10.10.2" )
        self . assertEqual ( result , "Second" )

class  TestNetworkInterface ( unittest . TestCase ):
    "" "Test: computer address" ""
    def  test_set_net ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        address  =  "1.2.3.4"
        comp . get_interface (). setNet ( net , address )
        result  =  comp . get_interface (). address
        self . assertEqual ( result , "1.2.3.4" )

    "" "Test: install DNS server" ""
    def  test_set_dns ( self ):
        comp  =  Computer ( "First" )
        address  =  "8.8.8.8"
        comp . get_interface (). setDns ( address )
        result  =  comp . get_interface (). dns
        self . assertEqual ( result , "8.8.8.8" )

    "" "Test: disconnect from the network" ""
    def  test_disconnect ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        comp . get_interface (). disconnect ()
        result  =  comp . get_interface (). address
        self . assertEqual ( result , None )
        result  =  comp . get_interface (). net
        self . assertEqual ( result , None )

    "" "Test: getting DNS from a network without a network" ""
    def  test_get_dns_without_net ( self ):
        comp  =  Computer ( "First" )
        result  =  comp . get_interface (). get_dns ()
        self . assertEqual ( result , "No network" )

    "" "Test: getting an" empty "DNS from the network" ""
    def  test_get_empty_dns ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        comp . get_interface (). get_dns ()
        result  =  comp . get_interface (). dns
        self . assertEqual ( result , "No DNS" )

    "" "Test: getting DNS from the network" ""
    def  test_get_dns ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        net . set_dns ( "8.8.8.8" )
        comp . get_interface (). get_dns ()
        result  =  comp . get_interface (). dns
        self . assertEqual ( result , "8.8.8.8" )

class  TestNetwork ( unittest . TestCase ):
    "" "Test: the number of hosts on the network" ""
    def  test_hosts_num ( self ):
        comp1  =  Computer ( "First" )
        comp2  =  Computer ( "Second" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        net . add_host ( comp2 , "172.10.10.2" )
        result  =  net . get_hosts_num ()
        self . assertEqual ( result , 2 )
        comp3  =  Computer ( "Third" )
        net . add_host ( comp3 , "172.10.10.3" )
        result  =  net . get_hosts_num ()
        self . assertEqual ( result , 3 )

    "" "Test: add a computer with a busy address" ""
    def  test_busy_address ( self ):
        comp1  =  Computer ( "First" )
        comp2  =  Computer ( "Second" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        result  =  net . add_host ( comp2 , "172.10.10.1" )
        self . assertEqual ( result , "Busy address" )

    "" "Test: re-add a computer with a different address" ""
    def  test_rewrite_address ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        net . add_host ( comp , "172.10.10.2" )
        result  =  comp . get_interface (). address
        self . assertEqual ( result , "172.10.10.2" )
        result  =  net . get_hosts_num ()
        self . assertEqual ( result , 1 )

    "" "Test: resolving the name of a non-existent computer" ""
    def  test_resolve_unk_host ( self ):
        net  =  Network ()
        address  =  "1.2.3.4"
        result  =  net . net_resolve ( address )
        self . assertEqual ( result , "Unknown host" )

    "" "Test: Resolve Computer Name" ""
    def  test_resolve_host ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        result  =  net . net_resolve ( comp . get_interface (). address )
        self . assertEqual ( result , "First" )

    "" "Test: Resolve the computer name on the network" ""
    def  test_local_resolve ( self ):
        comp1  =  Computer ( "First" )
        comp2  =  Computer ( "Second" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        net . add_host ( comp2 , "172.10.10.2" )
        result  =  comp1 . get_interface (). local_resolve ( "172.10.10.2" )
        self . assertEqual ( result , "Second" )

    "" "Test: Send a message" ""
    def  test_send_msg ( self ):
        comp1  =  Computer ( "First" )
        comp2  =  Computer ( "Second" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        net . add_host ( comp2 , "172.10.10.2" )
        comp1 . form_msg ( "172.10.10.2" , "ICQ" , "OLOLO" )
        result  =  comp2 . all_data [ len ( comp2 . all_data ) - 1 ]. get_data ()
        self . assertEqual ( result , "OLOLO" )

    "" "Test: receiving a sent message after connecting" ""
    def  test_get_msg_after_connect ( self ):
        comp1  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . form_msg ( "172.10.10.2" , "ICQ" , "abcde" )
        result  =  net . num_msgs ()
        self . assertEqual ( result , 1 )
        comp2  =  Computer ( "Second" )
        net . add_host ( comp2 , "172.10.10.2" )
        result  =  net . num_msgs ()
        self . assertEqual ( result , 0 )
        result  =  comp2 . all_data [ len ( comp2 . all_data ) - 1 ]. get_data ()
        self . assertEqual ( result , "abcde" )

    "" "Test: Request a message from an empty queue" ""
    def  test_no_messages ( self ):
        comp1  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        result  =  comp1 . find_msg ()
        self . assertEqual ( result , "No messages" )

if  __name__  ==  '__main__' :
    unittest . main ()
