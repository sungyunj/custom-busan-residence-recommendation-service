# 스타벅스 데이터 운용 예제 코드

import pandas as pd
import requests

gu=pd.read_html('https://inasie.github.io/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/5/',encoding='utf-8')[0]
seoul=gu[gu['법정동주소'].str.contains('서울')][1:]

api="efc1b26d609b687398664b4f30490c20"

starbucks=[]
for q in seoul['법정동주소']:
    query= q+' 스타벅스'
    for i in range(1,46):
        url = f'''https://dapi.kakao.com/v2/local/search/keyword?query={query}&page={i}&size=15&category_group_code'''
        headers = {
            "Authorization": f"KakaoAK {api}"
        }
        places = requests.get(url, headers = headers).json()['documents']
        starbucks.extend(places)
sb=pd.DataFrame(starbucks)
sb=sb.drop_duplicates('place_name',keep='last')
sb=sb[sb['address_name'].str.contains('서울')]

print("반 진행")
starbucksr=[]
for q in seoul['법정동주소']:
    query= q+' 스타벅스 리저브'
    for i in range(1,46):
        url = f'''https://dapi.kakao.com/v2/local/search/keyword?query={query}&page={i}&size=15&category_group_code'''
        headers = {
            "Authorization": f"KakaoAK {api}"
        }
        places = requests.get(url, headers = headers).json()['documents']
        starbucksr.extend(places)
sbr=pd.DataFrame(starbucksr)
sbr=sbr[sbr['place_name'].str.contains('R')].drop_duplicates()
sbr=sbr[sbr['address_name'].str.contains('서울')]

bucks=pd.concat([sb,sbr],axis=0)
bucks=bucks.drop_duplicates(['address_name'],keep='last')
print(bucks)
bucks.to_csv('starbucks.csv', index=False)