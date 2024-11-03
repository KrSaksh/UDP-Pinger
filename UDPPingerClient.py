from socket import * # type: ignore
import time

srvrName = ''
srvrPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

rtts = []
loss = 0

for i in range(1, 11):

    try:
        start = time.time() 
        message = f"Ping {i} {start:.3f}"
        
        clientSocket.sendto(message.encode(), (srvrName, srvrPort))
        resp, srvrAddr = clientSocket.recvfrom(1024)

        end = time.time()

        rtt = end - start
        rtts.append(rtt)
        
        print(f"Got response from {srvrName}: {resp.decode()} | RTT: {rtt:.3f} seconds")
        
    except timeout:
        print("Request timed out")
        loss += 1

clientSocket.close()
