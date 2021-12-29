import  unittest
from  general  import genral 
from  dns  import dns 


class  TestDns ( unittest . TestCase ):
    "" "Test: records in an empty database" ""
    def  test_empty_dns ( self ):
        d1  =  DnsRecursive ()
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        d1 . set_host ( cd1 )
        result  =  d1 . db . num_records ()
        self . assertEqual ( result , 0 )

    "" "Test: Add a record to the database" ""
    def  test_add_dns_record ( self ):
        d1  =  DnsRecursive ()
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        d1 . set_host ( cd1 )
        d1 . db . form_record ( "ya.ru" , "10.20.30.40" )
        result  =  d1 . db . num_records ()
        self . assertEqual ( result , 1 )

    "" "Test: deleting a record from the database" ""
    def  test_delete_dns_record ( self ):
        d1  =  DnsRecursive ()
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        d1 . set_host ( cd1 )
        d1 . db . form_record ( "ya.ru" , "10.20.30.40" )
        result  =  d1 . db . num_records ()
        self . assertEqual ( result , 1 )
        d1 . db . delete_record ( "ya.ru" )
        result  =  d1 . db . num_records ()
        self . assertEqual ( result , 0 )

    "" "Test: Resolving name from empty databases recursively" ""
    def  test_resolve_blank_dns_recursive ( self ):
        comp1  =  Computer ( "First" )
        d1  =  DnsRecursive ()
        d2  =  DnsRecursive ()
        d1 . set_dns ( "8.8.4.4" )
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        cd2  =  Computer ( "cd2" )
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2 )
        net  =  Network ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1 , "8.8.8.8" )
        net . add_host ( cd2 , "8.8.4.4" )
        result  =  comp1 . resolve ( "any" )
        self . assertEqual ( result , "Unknown host" )

    "" "Test: Resolving the name from the first database recursively" ""
    def  test_resolve_1st_dns_recursive ( self ):
        comp1  =  Computer ( "First" )
        d1  =  DnsRecursive ()
        d2  =  DnsRecursive ()
        d1 . set_dns ( "8.8.4.4" )
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        cd2  =  Computer ( "cd2" )
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2 )
        net  =  Network ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1 , "8.8.8.8" )
        net . add_host ( cd2 , "8.8.4.4" )
        d1 . db . form_record ( "google.com" , "1.2.3.4" )
        result  =  comp1 . resolve ( "google.com" )
        self . assertEqual ( result , "1.2.3.4" )

    "" "Test: Resolve name from second database recursively" ""
    def  test_resolve_2nd_dns_recursive ( self ):
        comp1  =  Computer ( "First" )
        d1  =  DnsRecursive ()
        d2  =  DnsRecursive ()
        d1 . set_dns ( "8.8.4.4" )
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        cd2  =  Computer ( "cd2" )
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2 )
        net  =  Network ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1 , "8.8.8.8" )
        net . add_host ( cd2 , "8.8.4.4" )
        d2 . db . form_record ( "google.com" , "1.2.3.4" )
        result  =  comp1 . resolve ( "google.com" )
        self . assertEqual ( result , "1.2.3.4" )

    "" "Test: resolving name from empty databases non-recursively" ""
    def  test_resolve_blank_dns_nonrecursive ( self ):
        comp1  =  Computer ( "First" )
        d1  =  DnsNonRecursive ()
        d2  =  DnsNonRecursive ()
        d1 . set_dns ( "8.8.4.4" )
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        cd2  =  Computer ( "cd2" )
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2 )
        net  =  Network ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1 , "8.8.8.8" )
        net . add_host ( cd2 , "8.8.4.4" )
        result  =  comp1 . resolve ( "any" )
        self . assertEqual ( result , "Unknown host" )

    "" "Test: Resolving name from first database non-recursively" ""
    def  test_resolve_1st_dns_nonrecursive ( self ):
        comp1  =  Computer ( "First" )
        d1  =  DnsNonRecursive ()
        d2  =  DnsNonRecursive ()
        d1 . set_dns ( "8.8.4.4" )
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        cd2  =  Computer ( "cd2" )
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2 )
        net  =  Network ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1 , "8.8.8.8" )
        net . add_host ( cd2 , "8.8.4.4" )
        d1 . db . form_record ( "google.com" , "1.2.3.4" )
        result  =  comp1 . resolve ( "google.com" )
        self . assertEqual ( result , "1.2.3.4" )

    "" "Test: Resolving name from second database non-recursively" ""
    def  test_resolve_2nd_dns_nonrecursive ( self ):
        comp1  =  Computer ( "First" )
        d1  =  DnsNonRecursive ()
        d2  =  DnsNonRecursive ()
        d1 . set_dns ( "8.8.4.4" )
        cd1  =  Computer ( "cd1" )
        cd1 . get_service ( d1 )
        cd2  =  Computer ( "cd2" )
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2 )
        net  =  Network ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1 , "8.8.8.8" )
        net . add_host ( cd2 , "8.8.4.4" )
        d2 . db . form_record ( "google.com" , "1.2.3.4" )
        result  =  comp1 . resolve ( "google.com" )
        self . assertEqual ( result , "1.2.3.4" )


if  __name__  ==  '__main__' :
    unittest . main ()
