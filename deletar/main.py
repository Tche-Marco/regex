from typing import Dict
import requests
import re
import pandas as pd
from datetime import datetime
import time


def salva_valor() -> Dict:
    usd_request = requests.get(
        "https://economia.awesomeapi.com.br/json/daily/USD-BRL/3")
    btc_request = requests.get(
        "https://economia.awesomeapi.com.br/json/daily/BTC-BRL/3")

    valores = {
        'USD': usd_request.json(),
        'BTC': btc_request.json()[0]
    }

    return valores


def valores_agora() -> Dict:
    url_valores = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL")
    valores_json = url_valores.json()

    valores = {
        'USD': valores_json["USDBRL"],
        'BTC': valores_json["BTCBRL"]
    }

    return valores


salva_valor = salva_valor()
print(salva_valor['USD'])
# print(valores_ontem['BTC'])

valores_agora = valores_agora()
print(valores_agora['USD']["bid"])
# print(valores_agora['BTC'])


#     time.sleep(1800)


def ultimas_noticias_uol():
    url_uol = "https://noticias.uol.com.br/ultimas/"
    html_uol = requests.get(url_uol).text
    noticias_uol = re.findall(
        r'<h3 class="thumb-title title-xsmall title-lg-small"[^>]*>(.*?)</h3>', html_uol)
    return noticias_uol


def ultimas_noticias_g1():
    url_g1 = "https://g1.globo.com/"
    html_g1 = requests.get(url_g1).text
    noticias_g1 = re.findall(
        r'<a[^>]*class="feed-post-link gui-color-primary gui-color-hover"[^>]*>(.*?)</a>', html_g1)
    return noticias_g1


noticias = 'UOL:\n'
for i in ultimas_noticias_uol():
    noticias += i+'\n\n'

noticias += 'g1:\n'

for i in ultimas_noticias_g1():
    noticias += i+'\n\n'

print(noticias)

# Significado regex [^>]* ==> aceita qualquer caractere diferente de '>' e o asterisco
# representa que a expressão anterior pode acontecer 0 ou infinitas vezes
# Significado regex (.*?) ==>
