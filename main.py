from .script import runddos, run_sms, runping, pc_attack
import datetime as dt
import platform
from data.check_connection import test_connection
def menu():

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


if __name__ == '__main__':
    if test_connection():
        menu()
    else:
        print("Internet bilan aloqa mavjud emas❌")