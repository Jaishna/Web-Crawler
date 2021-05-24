import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        website = input("Enter website- ")
        url = website + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html5lib')
        for link in soup.findAll('a', ):
            href = str(website) + link.get('href')
            title = link.string
            print(title)
            print(href)
            get_single_item(href)
        page += 1


def get_single_item(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html5lib')
    for item_name in soup.findAll('a', ):
        link = str(item_url)+item_name.get('href')
        print(link)


trade_spider(5)
