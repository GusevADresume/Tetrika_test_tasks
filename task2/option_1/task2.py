import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict


def find_all_animals() -> None:
    base_url = 'https://ru.wikipedia.org'
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    while url != '':
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            all_animals_in_page = soup.find('div', {'class': 'mw-category mw-category-columns'}).text
            animal_counting(all_animals_in_page)
            next_page = soup.find('a', text=re.compile('Следующая страница'))
            url = base_url+next_page['href']
        except:
            break



def animal_counting(all_animals_in_page) -> None:
    for animal in all_animals_in_page.split('\n'):
        if len(animal) > 1:
            if animal[0] in final_dict.keys():
                final_dict[animal[0]] += 1
            else:
                final_dict[animal[0]] = 1

def clean_dict() -> None:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ord_dict = OrderedDict(final_dict)
    for key in ord_dict.keys():
        if bool(set(alphabet).intersection(set(key.lower()))):
            del final_dict[key]



final_dict = {}
find_all_animals()
clean_dict()
print(final_dict)