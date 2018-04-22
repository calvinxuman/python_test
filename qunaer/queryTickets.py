# *-* coding:UTF-8  *-*

import requests
dptStation='武汉'
arrStation='深圳'
date='2017-12-15'
url="https://train.qunar.com/dict/open/s2s.do?dptStation=武汉&arrStation=长沙&date=2017-12-25&type=normal&user=neibu&source=site&start=1&num=500"

r=requests.get(url)
d=list(r.json()['data']['s2sBeanList'])
n=1
for i in d:
    print(n,i['trainNo'],i['dptStationName'],i['arrStationName'],i['dptTime'],i['arrTime'],i['extraBeanMap']['interval'],i['seats'].get('无座'))
    n += 1


