import socket
import time
UDP_IP = "127.0.0.1"
UDP_PORT = 54569
MSG = b"Hello, World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packets = 100
print("Sending {} packets to {} : {}".format(packets,UDP_IP,UDP_PORT))

count = 0
while True:
    count += 1
    sock.sendto(MSG,(UDP_IP, UDP_PORT))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S",t)
    print("{} sent packet {}/{} to {}:{}".format(current_time, count, packets, UDP_IP,UDP_PORT))
    if count>packets:
        break
    time.sleep(2)

print("Done.")

