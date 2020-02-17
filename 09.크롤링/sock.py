import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip, 80))   # 80 : http, 443 : https

sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)    # 4096 bytes 만 받아온다.
buffer = buffer.decode().replace("\r\n", "\n")
sock.close()

print(buffer)


