from socket import * 


def traceroute(destIP):
	print 'Start Traceroute with destIP:',destIP

	#Ports: 33434 , 33534
	Port = 33434	

	#Address of Destination:
	addr = (destIP,Port)
	max_hops = 30

#Translate an Internet protocol name to a constant suitable for passing as the (optional) third argument to the socket() function 	
	icmp = getprotobyname('icmp')
	udp = getprotobyname('udp')
	
	ttl = 1
	Current_IP = None

	while (Current_IP != destIP) and (ttl < max_hops):

# Create 2 sockets:
# One ICMP Socket wich recieves the ICMP msgs
# One UDP Socket wich sends a UDP msg
		Recieve_Socket = socket(AF_INET, SOCK_RAW , icmp)

#Recieve_Socket.bind(("", Port))
		Recieve_Socket.settimeout(1)	

		Send_Socket = socket(AF_INET, SOCK_DGRAM, udp)
#The setsockopt() function manipulates options associated with a socket. 
# Options affect socket operations, such as the routing of packets, out-of-band data transfer, and so on. 
		Send_Socket.setsockopt(SOL_IP, IP_TTL, ttl)

		Send_Socket.sendto("", addr)

		try:
			data, Current_Addr = Recieve_Socket.recvfrom(512)
			Current_IP = Current_Addr[0]
			ttl += 1
		
		except timeout:
			pass
		except error:
			pass
		finally:
			Send_Socket.close()
			Recieve_Socket.close()
		
	return (ttl-1)