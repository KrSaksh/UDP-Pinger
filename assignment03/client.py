from socket import *
import time
import random

srvrName = '192.168.49.117'
srvrPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
T1, T2 = 0.1, 0.5

# GBN parameters
window_size = 7
base = 0
next_seq_num = 1
num_packets = 50
drop_probability = 0.25 


rtts = []
loss = 0

while base < num_packets:

    while next_seq_num < base + window_size and next_seq_num < num_packets:
        message = f"SeqNo: {next_seq_num} Time: {time.time()}"
        if random.random() > drop_probability:  # Simulate drop probability
            clientSocket.sendto(message.encode(), (srvrName, srvrPort))
            print(f"Sent packet with SeqNo: {next_seq_num}")
        else: 
            loss += 1
        next_seq_num += 1
        
    start = time.time() * 1000

    try:
        resp, srvrAddr = clientSocket.recvfrom(1024)
        end = time.time() * 1000
        rtt = (end - start)
        rtts.append(rtt)
        ack_num = int(resp.decode().split(":")[1])
        
        if base <= ack_num < base + window_size:
            base = ack_num + 1
            print(f"Received ACK for SeqNo: {ack_num} | RTT: {rtt:.3f} ms")
        else:
            print("Received out-of-order ACK or duplicate")

    except timeout:
        print("Timeout - retransmitting window")
        next_seq_num = base
    time.sleep(random.uniform(T1, T2))

# if rtts:
#     print(f"\n--- {srvrName} ping statistics ---")
#     print(f"{num_packets} packets transmitted, {num_packets - loss} received, {(loss*100)/num_packets}% packet loss")
#     print(f"round-trip min/avg/max = {min(rtts):.3f}/{sum(rtts)/len(rtts):.3f}/{max(rtts):.3f} ms")

if rtts:
    print(f"\n--- {srvrName} ping statistics ---")
    print(f"{num_packets} packets transmitted, {num_packets - loss} received, {(loss*100)/num_packets}% packet loss")
    print(f"round-trip min/avg/max = {min(rtts):.3f}/{(sum(rtts)/len(rtts)):.3f}/{max(rtts):.3f} ms")    

print("Transmission completed")
clientSocket.close()