from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

expected_seq_num = 0
drop_probability = 0.1  # Adjust to simulate packet loss

while True:
    message, clientAddress = serverSocket.recvfrom(1024)
    
    if random.random() < drop_probability:  # Simulate packet loss
        print("Simulating packet drop")
        continue

    # Parse received packet sequence number
    seq_num = int(message.decode().split()[1].strip().split()[0])

    if seq_num == expected_seq_num:
        print(f"Received in-order packet with SeqNo: {seq_num}")
        expected_seq_num += 1
    else:
        print(f"Out-of-order packet received with SeqNo: {seq_num} (Expected: {expected_seq_num})")

    # Send an ACK for the last correctly received packet
    ack_message = f"ACK:{expected_seq_num - 1}"
    serverSocket.sendto(ack_message.encode(), clientAddress)
