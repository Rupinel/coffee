import requests
from bs4 import BeautifulSoup

url = 'http://www.hungryapp.co.kr/attack/attack_main.php'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
list = soup.find_all("li", class_="gbbs")

info = {}

for li in list:

    GAME_CD = li.find('a')['href'].split("=")[-1]
    GAME_NM = li.find('a').text.strip()

    info[GAME_CD] = GAME_NM

print(info)


