import requests
from bs4 import BeautifulSoup

url = 'http://www.hungryapp.co.kr/bbs/list.php?mode=&pid=&kfid=&btype=&bcode=aden&pgcode=&chamidx=&indexss=&catecode=&page=1&scode=&searchtype=subject&searchstr=&tcnt=&tbcnt=&block=&mn=&mx=&itemcode=&manager=&sdate=&edate='
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
list = soup.find_all("tr", class_="deftr")

for li in list:

    a = li.find('a')
    title = a.text.strip()
    time = li.find("span", class_="time today").text.strip()

    print(title, time)
