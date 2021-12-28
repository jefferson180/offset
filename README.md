# offset
 general.py Base library Includes classes:

Message:
implemented message transfer
messages are stored by the host
if the host is offline, the message is stored on the network (when connected to the network, the host automatically polls the network for messages)
the message carries protocol and data
Service:
implemented class for services
services store information about the computer on which they are running
each service has its own name
all services are stored in the dictionary of the host (the key is the name of the service)
Network interface:
computer network interface implemented
the network interface, as in real life, knows what DNS is (DNS basic interface setting)
the interface acts as a layer between the computer and the network
the interface has a disconnect function
the interface is able to request the address of the DNS server from the network
the interface will be able to send messages to the network
the interface can request messages from the network
Computer:
computer implemented
one way or another, almost all functions of the computer and the network interface are the same
the computer generates messages for further sending
Net:
network implemented
Primory DNS is installed on the network
the network can add and remove hosts
the network can ping
the network has the ability to resolve the connected computers without the involvement of DNS
the network receives messages from network interfaces and remembers them if the recipient is offline
the network sends a request to the DNS server about the resolution of the name test_general.py contains 21 tests of the base library
dns.py DNS Concept Includes classes:

Record:
DNS records implemented
Database:
The database is a name-address dictionary
The database can add and delete records
Recursive DNS service:
Recursive DNS service implemented
Non-recursive DNS service
Implemented non-recursive DNS service
Implemented response codes (0 - record found, 1 - record not found) test_dns.py contains 9 tests of the DNS concept
