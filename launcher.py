#!/bin/python3

print("""  

  _  __           _____ _____ _____   _____          
 | |/ /    /\    / ____|_   _|  __ \ / ____|   /\    
 | ' /    /  \  | (___   | | | |__) | |  __   /  \   
 |  <    / /\ \  \___ \  | | |  _  /| | |_ | / /\ \  
 | . \  / ____ \ ____) |_| |_| | \ \| |__| |/ ____ \ 
 |_|\_\/_/    \_\_____/|_____|_|  \_\\_____/_/    \_\
                                                     
                                                     
                

                  #Coded by Mert Daş
                                                     
""")

print("[!!! UYARI !!!] Öncelikle Açık Portları Taratıp , Ardından Açık Portların Ardındaki Servisleri Taramanız Önerilir !")
print("""
""")
print("1) Port Tarama : (Sadece Portların Açık-Kapalı Olduğunu Tarar)")
print("""
""")
print("2) Servis Tarama : ""(Portların Arkasında Çalışan Servisleri Tarar)")
print("""
""")
choice=input("Seçim : ")
if choice == '1':
	import scanner
	scanner.main()
if choice == '2':
	import grabber
	grabber.main()
