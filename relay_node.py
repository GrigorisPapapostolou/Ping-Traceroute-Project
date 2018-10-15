from ping import ping
from traceroute import traceroute
from socket import * 
import urllib



serverPort = 32422

if __name__ == "__main__":

	serverSocket = socket( AF_INET , SOCK_STREAM )
	serverSocket.bind(("",serverPort))
	serverSocket.listen(1)

	while 1:
		connectionSocket , addr = serverSocket.accept()
		
		command = connectionSocket.recv(64)
		print "Command is:",command		
		if command == 'results':
			print ' Results: '
			data = connectionSocket.recv(2048)
			print "Recieve Data :",data
			array = data.split(",")
			ServerIP = array[0]
			Pings = array[1]
			print 'EndServerIP:',ServerIP
			print 'Pings:',Pings

			max_pings = int(Pings)
			  
			RTT = ping(ServerIP, max_pings)
			hops = traceroute(ServerIP)
			print "The results : RTT = ",str(RTT)," hops = ",str(hops)
        		#Send Results 
			Send_data =str(RTT)+","+str(hops)
			connectionSocket.send(Send_data)

		elif command == 'file':
			print 'File : '
			url = connectionSocket.recv(512)
		 
			testfile = urllib.URLopener()
			testfile.retrieve(url,'file')
		        
			f = open('file','rb')
			l = f.read(1024)
			while (l):
		    		connectionSocket.send(l)
		    		l = f.read(1024)
	
			f.close()
			print "Done Sending"
			connectionSocket.shutdown(SHUT_WR)
	
		connectionSocket.close()

