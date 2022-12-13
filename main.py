import requests
from bs4 import BeautifulSoup
import lxml


urls = ['https://www.amazon.com/FIFA-23-Origin-Standard-Online/dp/B0BGJZ9WZW/ref=sr_1_1?crid=U619B43UDBA2&keywords=fifa+23&qid=1670934286&sprefix=fifa%2Caps%2C247&sr=8-1',
        'https://www.amazon.com/FIFA-Legacy-Switch-Region-Free-Nintendo/dp/B0B6CKG1MH/ref=sr_1_2?crid=U619B43UDBA2&keywords=fifa+23&qid=1670935268&sprefix=fifa%2Caps%2C247&sr=8-2',
        'https://www.amazon.com/FIFA-23-Steam-Ultimate-Online/dp/B0BGJZFRH7/ref=sr_1_3?crid=U619B43UDBA2&keywords=fifa+23&qid=1670935268&sprefix=fifa%2Caps%2C247&sr=8-3',
        ]
def get_link_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept-Language': 'en',
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    name = soup.select_one(selector='#productTitle').getText()
    name = name.strip()
    print(name)
    price = soup.select_one(selector='#priceblock_ourprice').getText()
    price = float(price[1:])
    print(price)

for url in urls:
    get_link_data(url)