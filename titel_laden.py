import requests
from bs4 import BeautifulSoup

datei = open('ListeFilme', 'a+')
kategorien = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J-K','L', 'M', 'N-O', 'P', 'Q-R', 'S', 'T', 'U-W', 'X-Z']

for kategorie in kategorien:
    url = 'https://en.wikipedia.org/wiki/List_of_films:_' + kategorie
    website = requests.get(url)
    results = BeautifulSoup(website.content, 'html.parser')
    results = results.find_all('i')
    for li in results:
        li = str(li)
        try:
            if 'href' in li:
                li = str(li).split('>')[2].split('<')[0]
                datei.write(li + '\n')
            else:
                li = str(li).split('<i>')[2].split('</i>')[0]
                print(li)
        except:
            pass