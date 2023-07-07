import requests
from bs4 import BeautifulSoup

url = 'https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry'
#url = 'https://stock.mk.co.kr/domestic/all_stocks?type=kosdaq&status=industry'

response = requests.get(url)
#print("response", response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

# items = soup.find_all('li', class_='row_sty')  # 'li' 태그에서 class가 'row_sty'인 요소들을 모두 찾음

# for item in items:
#     name = item.find(class_='name').text.strip()  # 'name' 클래스에서 텍스트 추출
#     print("Name:", name)
#     codes = item.find('a')['href']
#     if codes:
#         code = codes.split('/')[-1]
#         print("Code:",code)
#
#     price = item.find(class_='price').text.strip()  # 'price' 클래스에서 텍스트 추출
#     print("Price:", price, "\n")
    
row_stys = soup.select(".row_sty")
for idx,rs in enumerate(row_stys):
    s_code = rs.select("a")[0]['href'].split("/")[3]
    s_name = rs.select("a")[0].text.strip()
    price = rs.select(".st_price")[0].text.strip()
    print(idx+1, s_code, s_name, price)