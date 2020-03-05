#!/bin/bash

import sys
import socket
from datetime import datetime
yesil = "\033[32m"
varsa = "\033[0m"

print("""  

  _  __           _____ _____ _____   _____          
 | |/ /    /\    / ____|_   _|  __ \ / ____|   /\    
 | ' /    /  \  | (___   | | | |__) | |  __   /  \   
 |  <    / /\ \  \___ \  | | |  _  /| | |_ | / /\ \  
 | . \  / ____ \ ____) |_| |_| | \ \| |__| |/ ____ \ 
 |_|\_\/_/    \_\_____/|_____|_|  \_\\_____/_/    \_\
                                                     
                                                     Port Tarama Aracı v1
                                                     
                                                     
                

                  #Coded by Mert Daş
                                                     
""")


if len(sys.argv) == 2:
     target = socket.gethostbyname(sys.argv[1]) 
else:
     print(yesil+"[+]Şu komutu girmelisiniz : python3 scanner.py <ip adresi ya da website ismi '\n' orn:google.com>")


print("-" * 50)
print("Hedef taranıyor.... "+target)
print("Başlama Tarihi: "+str(datetime.now()))
print("-" * 50)

try: 
	for port in range(21,65535): 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print("{}. Port kontrol ediliyor..".format(port))
		if result == 0: 
        		print("[+]{}. Port Açık".format(port))
		s.close()



except KeyboardInterrupt:
	print("\n[+]Programdan çıkılıyor")
	print("Bitti..")
	sys.exit()
except socket.gaierror:
	print("Ana bilgisayar adı çözümlenemedi..")
	sys.exit()
except socket.error:
	print("Sunucuya bağlanamadı")
	sys.exit()

