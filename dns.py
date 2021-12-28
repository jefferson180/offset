from  general  import  *

class  Record :
    "" "Initialize record" ""
    def  __init__ ( self ):
        self . name  =  None
        self . address  =  None

    "" "Setting the name of the entry" ""
    def  set_name ( self , name ):
        self . name  =  name

    "" "Setting the write address" ""
    def  set_address ( self , address ):
        self . address  =  address

    "" "Get the name of the entry" ""
    def  get_name ( self ):
        return  self . name

    "" "Get the address of the record" ""
    def  get_address ( self ):
        return  self . address

class  Database :
    "" "Initializing the Record Database" ""
    def  __init__ ( self ):
        self . records  = {}

    "" "Checking the presence of a record in the database" ""
    def  check_record ( self , name ):
        if  name  in  self . records :
            return  True
        return  False

    "" "Adding a record to the database" ""
    def  add_record ( self , record : Record ):
        if  self . check_record ( record ):
            self . delete_record ( record . get_name ())
        self . records [ record . get_name ()] =  record . get_address ()

    "" "Removing a record from the database" ""
    def  delete_record ( self , name ):
        if  self . check_record ( name ):
            self . records . pop ( name )
        else :
            return  "No record"

    "" "Checking the number of records in the database" ""
    def  num_records ( self ):
        return  len ( self . records )

    "" "Resolve from database named" ""
    def  resolve ( self , name ):
        if  self . check_record ( name ):
            return  self . records [ name ]
        return  False

    "" "Forming a record and writing a record to a record (record)" ""
    def  form_record ( self , name , address ):
        record  =  Record ()
        record . set_name ( name )
        record . set_address ( address )
        self . add_record ( record )

class  DnsRecursive ( Service ):
    "" "Initialize recursive DNS" ""
    def  __init__ ( self ):
        super (). __init__ ()
        self . db  =  Database ()
        self . dns  =  None
        self . set_name ( "DNS" )

    "" "Setting the DNS address for the service" ""
    def  set_dns ( self , address ):
        self . dns  =  address

    "" "Resolving database records and recursive search" ""
    def  resolve ( self , name ):
        if  not  self . db . resolve ( name ):
            return  self . find ( name )
        return  self . db . resolve ( name )

    "" "Recursive Record Search" ""
    def  find ( self , name ):
        if  not  self . dns :
            return  "Unknown host"
        return  self . get_host (). get_interface (). net . hosts [ self . dns ]. services [ "DNS" ]. resolve ( name )

    "" "Getting the search code (0 - found, 1 - not found)" ""
    def  get_code ( self , name ):
        return  0

class  DnsNonRecursive ( Service ):
    def  __init__ ( self ):
        super (). __init__ ()
        self . db  =  Database ()
        self . dns  =  None
        self . set_name ( "DNS" )

    "" "Setting the DNS address for the service" ""
    def  set_dns ( self , address ):
        self . dns  =  address

    "" "Non-italic record search" ""
    def  resolve ( self , name ):
        if  self . db . resolve ( name ):
            return  self . db . resolve ( name )
        return  self . dns

    "" "Getting the search code (0 - found, 1 - not found)" ""
    def  get_code ( self , name ):
        if  self . db . resolve ( name ):
            return  0
        return  1
