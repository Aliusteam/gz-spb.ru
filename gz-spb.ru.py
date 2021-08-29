from bs4 import BeautifulSoup
import requests
import csv
import os
import time  # для задержки

# МЕНЯЕМ ТОЛЬКО URL И ЦЕНУ offerPriceView

url = 'https://account.gz-spb.ru/login'

# params = {'login[username]': 'mexet777','login[password]': 'asdfadf34#$4d'}
datas = {"login[username]": "mexet777", "login[password]": "asdfadf34#$4d"}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
           'accept': '*/*'}
s = requests.Session()
loging = s.post(url, data=datas, headers=HEADERS)
# print(loging.text)
# Переходим на страничку подачи предложений
url = 'https://estore.gz-spb.ru/electronicshop/offer/create/97884?backurl=L3Byb2NlZHVyZS9mb3JtL3ZpZXcvOTc4ODQv'

params = {
    'offer[offerRows][items][0][positionName]': 'Согласно документации',
    'offer[offerRows][items][0][warranty]': 'aafgadfadf',
    'offer[offerRows][items][0][offerPriceView]': '4020.00',
    'offer[offerRows][items][0][offerPriceNdsView]': '4020.00',
    'offer[offerRows][items][0][offerNds]': '0.00',
    "signAndSubmit": "Подписать+и+отправить",
    "offer[offerId]": ""
    , "offer[supplier][id]": "21056"
    , "offer[offerRows][items][0][positionItemId]": ""
    , "offer[offerRows][items][0][planPositionId]": ""
    , "offer[offerRows][items][0][offerRowId]": ""
}
loging = s.post(url, params=params, headers=HEADERS)
print(loging.text)
print(loging)
exit()
sys.exit()


# -------------------------------------------------
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
url = 'http://estore.gz-spb.ru/electronicshop/procedure/97998/search?backurl=L2VsZWN0cm9uaWNzaG9wL2NhdGFsb2cvcHJvY2VkdXJlL2luZGV4Lz9yZWVzdHJOdW1iZXI9MjAyMTAwMzIxOTYzMSZmdWxsU2VhcmNoPTAm&withNds=1&view=true'
s = requests.Session()
loging = s.get(url, headers=headers)
html = BeautifulSoup(loging.text, 'html.parser')

# while True:
cena = html.find('td', class_='row-priceNds').text
print(cena)
itog = ''
s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
for x in cena:
    if x in s:
        itog += x
    #    elif x == '.':
    #     break
    continue
print(float(itog) - 0.01)
