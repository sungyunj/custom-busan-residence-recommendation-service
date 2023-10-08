# 내가 살고 있는 집 주소 위도/ 경도

# 아직 키에러 뜨는 코드ㅠㅠ 왜그런거죠

import json
import requests
import pandas as pd

# from PyKakao import Karlo
# api = Karlo(service_key="efc1b26d609b687398664b4f30490c20")

addr = '인천시 남동구 운연천로11'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
headers = {'Authorization': 'KakaoAk ~'}

result = json.loads(str(requests.get(url, headers=headers).text))
x = result['documents'][0]['address']['×']
y = result['documents'][0]['address ']['y']


# 집 주소 반경 30km 이내 편의점 리스트 추출
convs = {}
for i in range(1, 46):
    headers = {
        "Authorization": "efc1b26d609b687398664b4f30490c20"
    }
    params = {
        'x': float(x),
        'y': float(y),
        'radius': 3000,
        'page': i,
        'size': 15,
        'sort': 'distance'
    }

    keywords = '편의점'
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(
        keywords)
    places = requests.get(url, headers=headers, params=params) . json()[
        'documents']
    if places == []:
        break
    else:
        convs[i] = places
places_name = []
brands = []
for i in range(1, len(convs)):
    for a in range(len(convs[i])):
        places_name.append(convs[i][a]['place name'])
names = list(set(places_name))
convin = pd.DataFrame()
convin['convin'] = names
