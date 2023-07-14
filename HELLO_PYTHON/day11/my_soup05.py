import requests
from bs4 import BeautifulSoup

url = 'https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry' 
#url = 'https://stock.mk.co.kr/domestic/all_stocks?type=kosdaq&status=industry'

response = requests.get(url)
#print("response", response.text)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
    
row_stys = soup.select(".row_sty")
for idx,rs in enumerate(row_stys):
    s_code = rs.select("a")[0]['href'].split("/")[3]
    s_name = rs.select("a")[0].text.strip()
    price = rs.select(".st_price")[0].text.strip()
    
    url2 = "https://stock.mk.co.kr/price/home/"+s_code
    response2 = requests.get(url2)
    html2 = response2.text
    soup2 = BeautifulSoup(html2, 'html.parser')
    
    tradingVolumn = soup2.select_one("span#trading_valume").text.strip()
    transactionAcmount = soup2.select_one("span#transaction_acmount").text.strip()
    
    table = soup2.select_one("table.noline_bottom")
    jabon = table.select("span.volume")[2].text.strip() #자본금
    sangjang = table.select("span.volume")[3].text.strip() #상장주식수
    siga = table.select("span.volume")[4].text.strip() #시가총액
    foreigner = table.select("span.volume")[5].text.split("%")[0].strip()+"%" #외국인보유
    
    print(idx, s_code, s_name, price, jabon, sangjang, siga, foreigner)
    # 주식코드, 주식명, 가격, 거래량, 거래대금, 자본금, 상장주식수, 시가총액, 외국인보유