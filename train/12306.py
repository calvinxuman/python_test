import requests

def getTrainInfo():
    response=requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-12-20&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT')
    return response.json()['data']['result']

for i in getTrainInfo():
    print(i)