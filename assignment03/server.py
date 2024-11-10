from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
T3, T4 = 0.1, 0.5

expected_seq_num = 0
drop_probability = 0.25 

while True:
    message, clientAddress = serverSocket.recvfrom(1024)
    
    if random.random() < drop_probability:
        print("Simulating packet drop")
        continue
    
    seq_num = int(message.decode().split()[1].strip().split()[0])
    time.sleep(random.uniform(T3, T4))

    if seq_num == expected_seq_num:
        print(f"Received in-order packet with SeqNo: {seq_num}")
        expected_seq_num += 1
    else:
        print(f"Out-of-order packet received with SeqNo: {seq_num} (Expected: {expected_seq_num})")

    ack_message = f"ACK:{expected_seq_num - 1}"
    serverSocket.sendto(ack_message.encode(), clientAddress)

