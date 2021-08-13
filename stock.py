import bs4
import requests
import winsound

url = 'https://finance.yahoo.com/quote/CLNE'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

price = soup.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print(price)

file = 'sound.mp3'

