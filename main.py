from urllib.request import urlopen
import requests
import json
import time
from datetime import datetime

with urlopen('https://api.coinmarketcap.com/v1/ticker/') as url:
    data = json.loads(url.read().decode())


myDict = {}
for item in data:
    myDict[item['id']] = []
running = True

while running:
    for i in range(80):
        item = data[i]
        try:
            cost = round(float(item['price_usd']), 2)
            myDict[item['id']].append(cost)
        except KeyError:
            pass
            
    if len(myDict[item['id']]) > 11:
        running = False
    
    time.sleep(300)

    with urlopen('https://api.coinmarketcap.com/v1/ticker/') as url:
        data = json.loads(url.read().decode())

    
    with open('data.json', 'w') as f:
        json.dump(myDict, f)
