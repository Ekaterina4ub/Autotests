#coding: utf-8

import requests

r = requests.get("https://staging-ipoteka.domclick.ru/mobile/v2/mortgage/calc?isIncomeSberbankCard=true&canConfirmIncome=false&productId=4&estateCost=3000000&deposit=1500000&term=120&isInsured=true&isMarried=false&isHusbandWifeLess35Years=false&children=0")
if r.status_code == 200:
    print("Расчет получен")
else:
    print("Всё сломалось")

r = requests.get("https://staging-ipoteka.domclick.ru/mobile/v2/mortgage/default")
if r.status_code == 200:
    print("Расчет по умолчанию получен")
else:
    print("Всё сломалось")

r = requests.post('https://qa-ipoteka.domclick.ru/mobile/v1/mortgage/calculation', data= {"estateCost":3000000})
if r.status_code == 200:
    print("Расчет создан")
else:
    print("Всё сломалось")