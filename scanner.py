import socket

ip = input("Enter the ip:")
ports = [i for i in range(1,65535+1)]


for port in ports:
    s = socket.socket()
    result = s.connect_ex((ip,port))
    if result == 0 :
        print(f"[+] {port} port is open")
        s.close()