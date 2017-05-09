#coding: utf-8

import requests

good_params = {
            'isIncomeSberbankCard': 'true',
            'canConfirmIncome' : 'false',
            'productId' : '4',
            'estateCost' : '3000000',
            'deposit' : '150000',
            'term' : '120',
            'isInsured' : 'true',
            'isMarried' : 'false',
            'isHusbandWifeLess35Years' : 'false',
            'children' : '0'
           }
bad_params = {
            'ghjdhg' : 1
             }

def check_response(response):
    if response.status_code == 200:
        print("Расчет получен")
    elif response.status_code == 404:
        print("Расчет не найден")
    elif response.status_code == 400:
        print("Неверный запрос")
    else:
        print("Что-то пошло не так")
    print(response.status_code)

# некорректный get-запрос
response = requests.get('https://ipoteka.domclick.ru/calculations/api/v1/mortgages/calculate', params=good_params)
check_response(response)

# корректный post-запрос без параметров
response = requests.post('https://ipoteka.domclick.ru/calculations/api/v1/mortgages/calculate')
check_response(response)

# корректный post-запрос с параметрами
response = requests.post('https://ipoteka.domclick.ru/calculations/api/v1/mortgages/calculate', params=good_params)
check_response(response)

# корректный post-запрос с некорректными параметрами
response = requests.post('https://ipoteka.domclick.ru/calculations/api/v1/mortgages/calculate', params=bad_params)
check_response(response)