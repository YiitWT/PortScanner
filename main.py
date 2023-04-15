import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("YIIT'S SCANNER")
print(ascii_banner)
target = input(str("Target ip: "))


print("-" * 50)
print("Scanning target", target)
print("Scanning started at: "+ str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        #Açık portu göster
        result = s.connect_ex((target, port))
        if result == 0:
            file = open("ports.txt", "w")
            print("[*] Port {} is open".format(port))
            file.write("[*] Port {} is open".format(port) + " ip: "+str(target)+"\n")
            file.close()
        s.close()
except KeyboardInterrupt:
    print("\n Kapatılıyor")
    sys.exit()

except socket.error:
    print("Host cevap vermeyi bıraktı :'(")
    sys.exit()
