import csv
import requests
from bs4 import BeautifulSoup

book=[]
def reding():
    url='https://books.toscrape.com/'
    respone=requests.get(url)

    if respone.status_code==200:
        print('Страница загружена')
        html=respone.text
        return html
    else:
        print('Ссылка не распознана')

def poisk(html):
    try:
        soup= BeautifulSoup(html,"lxml")
        cards =soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        print(f"Найдено карточек: {len(cards)} ")
        return cards
    except:
        print('Ошибка в нахождении карточек')

def name_book(cards):
    for i in range(len(cards)):
        name= cards[i]
        title=name.find("h3").find("a")
        titi=title.text.strip()
        price=name.find("p",class_="price_color")
        prici=price.text.strip()
        try:
            link= title.get("href")
            if link.startswith("catalogue/"):
                link="https://books.toscrape.com/"+ link
        except:
            link='нету ссылки'
        book.append({
            "Название:": titi,
            "Цена:": prici,
            "Ссылка:": link,
        })
    return book
def last_lvl(book):
    with open("books.csv","w",encoding="utf-8-sig",newline="") as f:
        fildname= ['Название:','Цена:','Ссылка:']
        writer=csv.DictWriter(f,fieldnames=fildname,delimiter=';')
        writer.writeheader()
        writer.writerows(book)
        print("Файл готов, находится в папке с кодом")
html=reding()
cards=poisk(html)
book=name_book(cards)
last_lvl(book)

