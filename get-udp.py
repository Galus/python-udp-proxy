import signal
import socket

IP = "127.0.0.1"
PORT = 54569
BUF = 50

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# s.settimeout(15)
s.bind((IP, PORT))

print("Listening on port {} from {}".format(PORT, IP))
while True:
    data, addr = s.recvfrom(BUF)
    if not data: break
    print("received:", data.decode(), "from:", addr)
    # s.send(data,
s.close()

