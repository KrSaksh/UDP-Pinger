import random
import time
from socket import * # type: ignore

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

while True:
        rand = random.randint(0,10)

        message, address = serverSocket.recvfrom(1024)
        

        mmss = time.strftime("%M:%S", time.localtime())
        mmss = mmss.split(':')
    
        
        end = float(mmss[0])*60 + float(mmss[1])
        
        decoded = message.decode().split()
        decode = decoded[2].split(':')
        hh = decode[0]
        mm = decode[1]
        ss = decode[2].split('.')
        ss = ss[0]
        ms = float(decode[2]) - float(ss)
        # print("decode: ", decode)
        # print("hh: ", hh)
        # print("mm: ", mm)
        # print("ss: ", ss)
        # print("ms: ", ms)
        time_diff_2 = abs(end - (float(mm)*60 + float(ss) + float(ms)))
        # time_diff = end_time - start_time
        
        msg_to_send = f"SeqNo: {decoded[1]} Time difference from timestamp: {time_diff_2:.4f} seconds"
        # print(f"Time difference from timestamp: {time_diff_2} seconds.\nTime difference: {time_diff} ms")


        if rand < 4:
            continue
        else:
            serverSocket.sendto(msg_to_send.encode(), address)
            
            