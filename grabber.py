#!/bin/python3

import socket

def banner(ip, port):
	s = socket.socket()
	s.connect((ip,int(port)))
	print(s.recv(1024))

print("""  

  _  __           _____ _____ _____   _____          
 | |/ /    /\    / ____|_   _|  __ \ / ____|   /\    
 | ' /    /  \  | (___   | | | |__) | |  __   /  \   
 |  <    / /\ \  \___ \  | | |  _  /| | |_ | / /\ \  
 | . \  / ____ \ ____) |_| |_| | \ \| |__| |/ ____ \ 
 |_|\_\/_/    \_\_____/|_____|_|  \_\\_____/_/    \_\
                                                     
                                                     Servis Tarama Aracı v1
                                                     
                                                     
                

                  #Coded by Mert Daş
                                                     
""")

def main():
	ip = input("Lütfen Ip adresi giriniz : ")
	port = str(input("Lütfen Port giriniz : " ))
	banner(ip, port)

main()

