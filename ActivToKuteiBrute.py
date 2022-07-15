import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, httpx
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
import random
from threading import active_count, Thread
import itertools
from colorama import Fore as f
from pystyle import Colorate, Colors, Write
import os

count = 0

# proxy = itertools.cycle(open('./proxy.txt').read())

prox = ["103.234.138.202:80", "116.66.198.228:80", "118.112.189.122:80", "140.133.76.200:80", "142.44.247.60:80", "141.0.11.253:80", "141.0.11.244:80", "141.0.11.243:80", "141.0.11.250:80", "146.185.135.27:8080", "159.65.83.216:80", "167.86.126.167:80", "178.132.2.178:80", "178.20.231.218:80", "180.179.13.135:80", "185.26.181.241:80", "190.128.227.98:80", "195.112.224.111:80", "195.30.107.52:80", "195.49.168.5:80", "195.88.152.77:80", "195.88.152.78:80", "195.83.197.222:80", "200.73.130.105:80", "202.4.186.102:80", "206.72.197.164:80", "209.197.68.107:80", "212.83.157.86:80", "213.197.182.102:80", "36.66.215.119:8080", "37.228.107.241:80", "37.228.107.253:80", "37.228.107.254:80", "45.77.23.119:80", "47.52.229.116:80", "72.249.51.52:80", "101.200.57.251:80", "117.54.238.66:8080", "141.0.11.254:80", "141.0.8.240:80", "141.0.11.241:80", "144.91.127.195:80", "160.16.216.195:80", "183.88.94.197:8080", "191.252.102.212:80", "206.72.201.203:80", "206.72.201.202:80", "141.0.8.24:80", "141.0.8.96:80", "140.227.25.56:5678", "103.117.192.14:80", "3.211.17.212:80"]

def gen():
    Red = random.randrange(150, 200, 2)
    Red2 = Red + random.randrange(11, 15, 2)
    Red3 = Red2 + random.randrange(11, 15, 2)
    Red4 = Red3 + random.randrange(11, 15, 2)
    Red5 = Red4 + random.randrange(11, 15, 2)
    Blue = random.randrange(150, 200, 2)
    Blue2 = Blue + random.randrange(11, 15, 2)
    Blue3 = Blue2 + random.randrange(11, 15, 2)
    Blue4 = Blue3 + random.randrange(11, 15, 2)
    Blue5 = Blue4 + random.randrange(11, 15, 2)
    Green = random.randrange(150, 200, 2)
    Green2 = Green + random.randrange(11, 23, 2)
    Green3 = Green2 + random.randrange(11, 23, 2)
    Green4 = Green3 + random.randrange(11, 23, 2)
    Green5 = Green4 + random.randrange(11, 23, 2)
    gurade = f"\x1b[38;2;{Red};{Green};{Blue}m"
    gurade2 = f"\x1b[38;2;{Red2};{Green2};{Blue2}m"
    gurade3 = f"\x1b[38;2;{Red3};{Green3};{Blue3}m"
    gurade4 = f"\x1b[38;2;{Red4};{Green4};{Blue4}m"
    gurade5 = f"\x1b[38;2;{Red5};{Green5};{Blue5}m"
    proxy = random.choice(prox)
    proxies = {
    "http":f"{proxy}"
    }
    testa = random.randrange(4, 6, 2)
    Test = '1234567890'
    invite = ''.join(random.choice(Test) for _ in range(7))
    #with httpx.Client(proxies= f"http://{proxy}" headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36','accept-language': 'ja,en-US;q=0.9,en;q=0.8'}) as htclient:
    req = requests.get(f'https://tokutei.cf/view/?q={invite}', proxies=proxies)
    url = f"https://tokutei.cf/view/?q={invite}"
    if req.status_code == 200:
        print(f'{Fore.LIGHTBLUE_EX}Fined Used invite! ->{Fore.RESET} ' + invite + f" Used Proxy {proxy}")
        f = open('usedurl.txt', 'a', encoding='UTF-8')
        f.write(f'{url}\n')
        f.close()
    elif req.status_code == 404:
        print(f'{Fore.LIGHTRED_EX}404 Not Found{Fore.RESET} -> {gurade}P{gurade2}r{gurade3}o{gurade4}x{gurade5}y = {proxy}{Fore.RESET}')
    elif req.status_code == 429:
        print('RateLimit Please wait 15min.')
        time.sleep(900)
    else:
        print(f'{Fore.RED}Error, Check Connection >{Fore.RESET} ' + invite + f" Used Proxy{proxy}\nStatus Code -> {req.status_code}")

if __name__ == "__main__":
    NThread = Write.Input("何threadにする?  -> ", Colors.red_to_purple, interval=0.00001)
#もう気にしなくていいよ	
    while True:
        Run = True
        while Run:
            if active_count() <= int(NThread):
                try:
                    Thread(target=gen).start()
                except:
                    pass
    else:
            if active_count() <= int(NThread):
                try:
                    Thread(target=gen).start()
                except:
                    pass