import requests
from bs4 import BeautifulSoup as BS


ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
main_domain = 'https://ru.wikipedia.org'

for lit in ALPHABET:
    r = requests.get(main_domain + '/w/index.php?title=Категория:Животные_по_алфавиту&from=' + lit)
    counter = 0

    while True:
        soup = BS(r.text, 'lxml')
        x = soup.find(id='mw-pages').find('div', class_='mw-category-group').find_all('a')

        if x[0].text.startswith(lit):
            counter += len(x)
        else:
            break

        next_page_url = soup.find('div', id='mw-pages').find_all('a')[1]['href']
        r = requests.get(main_domain + next_page_url)

    print(lit + ':', counter)
