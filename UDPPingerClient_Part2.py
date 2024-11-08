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
consecutive_losses = 0

for i in range(2000):

    if(consecutive_losses == 3): 
        print(f"\nAt SeqNo: {i-1}, After receiving {i-1-loss} packets, we encountered 3 consecutive losses.")
        break

    try:
        ist = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(ist)
        localTime = local_time.strftime("%H:%M:%S.%f")[:-3]

        message = f"SeqNo: {i} {localTime}"

        start = time.time() * 1000
        
        clientSocket.sendto(message.encode(), (srvrName, srvrPort))
        resp, srvrAddr = clientSocket.recvfrom(1024)

        end = time.time() * 1000
        
        rtt = end - start
        rtts.append(rtt)

        consecutive_losses = 0
        
        print(f"Got response from {srvrName} | RTT: {rtt:.3f} ms")
        print(f"Response: {resp.decode()}")

        

    except timeout:
        print("Request timed out")
        consecutive_losses += 1
        loss += 1


if rtts:
    print(f"\n--- {srvrName} ping statistics ---")
    print(f"{i-1} packets transmitted, {i-1-loss} received, {(loss*100)/(i-1)}% packet loss ")
    print(f"round-trip min/max/avg = {min(rtts):.3f}/{max(rtts):.3f}/{(sum(rtts)/len(rtts)):.3f} ms")    


clientSocket.close()
