import requests
from bs4 import BeautifulSoup

url = requests.get('https://finance.yahoo.com/quote/%5EGSPC/')
soup = BeautifulSoup(url.text, features="html.parser")

print(soup.find_all("div", {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}))