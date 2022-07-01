import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.yahoo.com/quote/TSLA?')
 
soup = BeautifulSoup(response.text, 'html.parser')

price = float(soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').get_text().replace(',', ''))
print(price)