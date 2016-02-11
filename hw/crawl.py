import requests

HOST = 'http://www.kobis.or.kr'
API_KEY = '60ff09dfb1818b290afaf0050a744c68'

def get_daily_boxoffice(target_dt):
    url = HOST + '/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    params = {
        'key': API_KEY,
        'targetDt': target_dt,
    }
    return requests.get(url, params=params).json()

print(get_daily_boxoffice('20160101'))
