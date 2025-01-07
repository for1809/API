# API란?
'''
Application Programming Interface의 약자로서
서로 다른 소프트웨어 기능들이 상호작용하는 규약(protocol)을 의미한다.
API는 Application이 정보 교환 요청을 하는데에 사용하는 메소드와 데이터 포맷을 정의하고
데이터 교환이 용이하도록 중개자 역할을 한다.
'''
import requests
import json

def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)

    if response.statuse_code == 200: # 정상적으로 요청이 됐는지 확인
        data = response.json()
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        price = data['Time Series (5min)'][last_refreshed]['1. open']
        return price
    else:
        return No