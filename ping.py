from socket import *
import time

def ping(destination,max_pings):
	print "Ping Function with : ",destination    
#Define a port number to "send"
	Port = 88
	addr = (destination , Port)

#Translate an Internet protocol name to a constant suitable for passing as the (optional) third argument to the socket() function
	icmp = getprotobyname('icmp')
	udp = getprotobyname('udp')

	pings = 0
	SumRTT = 0
    
	while (pings < max_pings):
	    Recieve_Socket = socket(AF_INET, SOCK_RAW, icmp)
        Send_Socket = socket(AF_INET, SOCK_DGRAM, udp)
	    
        Recieve_Socket.settimeout(1)	
        Send_Socket.sendto("",addr)
	    
	    start=time.time()
        
		try:
            data, server = Recieve_Socket.recvfrom(512)
            elapsed = (time.time()-start)
            SumRTT = SumRTT + elapsed
	    except timeout:
			pass
	    except error:
            pass
	    finally:
			Recieve_Socket.close()
            Send_Socket.close()
	
	    pings = pings + 1
	return SumRTT/max_pings
	



