from socket import *
import time
from datetime import timedelta, datetime
import pytz


srvrName = '192.168.49.117'
srvrPort = 12000



clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

rtts = []
loss = 0

for i in range(1, 11):
    
    
    try:
        ist = pytz.timezone('Asia/Kolkata')

        local_time = datetime.now(ist)
        localTime = local_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        # message = f"SeqNo: {i} {localTime}"

        # local_time = time.localtime()
        # ist_time = datetime(*local_time[:6]) + timedelta(hours=5, minutes=30)
        # localTime = ist_time.strftime("%H:%M:%S")
        
        message = f"Ping {i} {localTime}"
        
        start = time.time() * 1000

        clientSocket.sendto(message.encode(), (srvrName, srvrPort))
        resp, srvrAddr = clientSocket.recvfrom(1024)
       
        end = time.time() * 1000
        
        rtt = end - start
        rtts.append(rtt)
        
        #ye change krna h 
        print(f"Got response from {srvrName}: {resp.decode()} | RTT: {rtt:.3f} ms")
        

    except timeout:
        print("Request timed out")
        loss += 1


if rtts:
    print(f"\n--- {srvrName} ping statistics ---")
    print(f"{i} packets transmitted, {i-loss} received, {loss*10}% packet loss ")
    print(f"round-trip min/max/avg = {min(rtts):.3f}/{max(rtts):.3f}/{(sum(rtts)/len(rtts)):.3f} ms")    


clientSocket.close()
