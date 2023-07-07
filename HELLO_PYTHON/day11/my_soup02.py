import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/emp_list'

response = requests.get(url)
#print("response", response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select("tr")
for tr in trs:
    tds = tr.select("td")
    if tds:
        name_td = tds[1].text
        addr_td = tds[-1].text
        print(name_td, ',' ,addr_td)
