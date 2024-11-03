import random
from socket import * # type: ignore

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

while True:
    
	rand = random.randint(0,10)
	# rand = random.randint(1,10)
	message, address = serverSocket.recvfrom(1024)
	message = message.upper()

	if rand < 4:
		continue
	else:
		serverSocket.sendto(message, address)
