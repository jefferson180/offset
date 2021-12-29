class  Message :
    "" "Initialize message" ""
    def  __init__ ( self ):
        self . dst  =  None
        self . service  =  None
        self . data  =  None
    "" "Get message data" ""
    def  get_data ( self ):
        return  self . data

class  Service :
    "" "Service initialization" ""
    def  __init__ ( self ):
        self . host  =  None
        self . name  =  None

    "" "Setting the service name" ""
    def  set_name ( self , name ):
        self . name  =  name

    "" "Get service name" ""
    def  get_name ( self ):
        return  self . name

    "" "Setting the computer on which the service is running" ""
    def  set_host ( self , host ):
        self . host  =  host

    "" "Getting a computer running the service" ""
    def  get_host ( self ):
        return  self . host

class  NetworkInterface :
    "" "Initializing the network interface" ""
    def  __init__ ( self ):
        self . net  =  None
        self . address  =  None
        self . dns  =  None

    "" "Computer name resolution" ""
    def  local_resolve ( self , address ):
        return  self . net . net_resolve ( address )

    "" "Configuring the network for the network interface and polling the server for messages" ""
    def  setNet ( self , net , address ):
        if  self . net :
            self . disconnect ()
        self . net  =  net
        self . address  =  address
        self . net . find_msg ( self . address )

    "" "Set DNS server" ""
    def  setDns ( self , address ):
        self . dns  =  address

    "" "Disconnect from the network" ""
    def  disconnect ( self ):
        if  not  self . net :
            return  "No network"
        self . net . delete_host ( self . address )
        self . net  =  None
        self . address  =  None

    "" "Obtain DNS server address from the network" ""
    def  get_dns ( self ):
        if  not  self . net :
            return  "No network"
        self . dns  =  self . net . pull_dns ()

    "" "Ping" ""
    def  ping ( self , dst ):
        if  not  self . net :
            return  "No network"
        return  self . net . ping ( self . address , dst )

    """Send a message"""
    def  send_msg ( self , message : Message ):
        if  not  self . net :
            return  "No network"
        self . net . get_msg ( message )

    "" "Find a message on the network" ""
    def  find_msg ( self ):
        if  not  self . net :
            return  "No network"
        return  self . net . find_msg ( self . address )

    "" "Resolve name via DNS" ""
    def  resolve ( self , name ):
        if  not  self . dns :
            self . get_dns ()
        return  self . net . resolve ( name , self . dns )

class  Computer :
    "" "Initializing the computer" ""
    def  __init__ ( self , name ):
        self . interface  =  NetworkInterface ()
        self . name  =  name
        self . services  = {}
        self . all_data  = []

    "" "Get the computer's network interface" ""
    def  get_interface ( self ):
        return  self . interface

    "" "Get computer name" ""
    def  get_name ( self ):
        return  self . name

    "" "Resolve the name of a computer on the network" ""
    def  local_resolve ( self , address ):
        return  self . interface . local_resolve ( address )

    "" "Ping" ""
    def  ping ( self , address ):
        return  self . interface . ping ( address )

    "" "Install the service on the computer" ""
    def  get_service ( self , service : Service ):
        self . services [ service . get_name ()] =  service

    """Send a message"""
    def  send_msg ( self , message : Message ):
        self . interface . send_msg ( message )

    "" "Receive a message and write it to the repository" ""
    def  get_msg ( self , message : Message ):
        self . all_data . append ( message )

    "" "Search for messages on the network" ""
    def  find_msg ( self ):
        return  self . interface . find_msg ()

    "" "Generate a message and send it" ""
    def  form_msg ( self , dst , service , data ):
        msg  =  Message ()
        msg . dst  =  dst
        msg . service  =  service
        msg . data  =  data
        self . send_msg ( msg )

    "" "Resolve name via DNS" ""
    def  resolve ( self , name ):
        return  self . interface . resolve ( name )

class  Network :
    "" "Network initialization" ""
    def  __init__ ( self ):
        self . hosts  = {}
        self . dns  =  None
        self . msgs : dict [ str , Message ] = {}

    "" "Set a primary DNS server for the network" ""
    def  set_dns ( self , address ):
        self . dns  =  address

    "" "Give the address of the primary DNS server to the interface" ""
    def  pull_dns ( self ):
        if  not  self . dns :
            return  "No DNS"
        return  self . dns

    "" "Add a host to the network" ""
    def  add_host ( self , computer : Computer , address ):
        if  address  in  self . hosts :
            return  "Busy address"
        self . hosts [ address ] =  computer
        computer . get_interface (). setNet ( self , address )

    "" "Remove host from network" ""
    def  delete_host ( self , address ):
        self . hosts . pop ( address )

    "" "Ping" ""
    def  ping ( self , src_address , dst_address ):
        if  dst_address  in  self . hosts :
            return  f "Success ping from { src_address } to { dst_address } "
        return  "Unknown host"

    "" "Get the number of hosts on the network" ""
    def  get_hosts_num ( self ):
        return  len ( self . hosts )

    "" "Resolve the name of a computer on the network" ""
    def  net_resolve ( self , address ):
        if  address  in  self . hosts :
            return  self . hosts [ address ]. get_name ()
        return  "Unknown host"

    "" "Accept the message and transmit it or remember it" ""
    def  get_msg ( self , message : Message ):
        if  message . dst  in  self . hosts :
            self . hosts [ message . dst ]. get_msg ( message )
            return
        self . msgs [ message . dst ] =  message

    "" "Find a message by request" ""
    def  find_msg ( self , address ):
        if  address  in  self . msgs :
            self . hosts [ address ]. get_msg ( self . msgs [ address ])
            self . msgs . pop ( address )
            return
        return  "No messages"

    "" "Get the number of messages stored in the network" ""
    def  num_msgs ( self ):
        return  len ( self . msgs )

    "" "Resolve name via DNS" ""
    def  resolve ( self , name , dns ):
        if  not  dns :
            return  "Unknown host"
        status  =  self . hosts [ dns ]. services [ "DNS" ]. get_code ( name )
        if ( status  ==  1 ):
            return  self . resolve ( name , self . hosts [ dns ]. services [ "DNS" ]. resolve ( name ))
        return  self . hosts [ dns ]. services [ "DNS" ]. resolve ( name )
