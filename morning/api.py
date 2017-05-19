import requests
import json

# r = requests.request(method='GET', url='http://ya.ru')
#
# print(r.cookies)

# r = requests.request(method='POST', url='http://ya.ru', headers={'Content-Type':'application/json',
#                                                                  'Request-Spec' : 'ghdhhdgsf'}) можно добавить путь к файлу (file= после })

def request_main(**kwargs):
    r = requests.request(method=kwargs['method'], url=kwargs['url'])
    return r

# print(request_main(method='GET', url='http://ya.ru').content)

def test_yandex():
    assert request_main(method='GET', url='http://ya.ru').status_code == 200

def test_google():
    assert request_main(method='GET', url='http://google.ru').status_code == 200

# r = requests.get(http//:127.0.0.1:8882, )

