from typing import Dict
import requests
import re
import pandas as pd
from datetime import datetime
import time


def valores_ontem() -> Dict:
    usd_request = requests.get(
        "https://economia.awesomeapi.com.br/json/daily/USD-BRL/2")
    eur_request = requests.get(
        "https://economia.awesomeapi.com.br/json/daily/EUR-BRL/2")
    btc_request = requests.get(
        "https://economia.awesomeapi.com.br/json/daily/BTC-BRL/2")

    valores = {
        'USD': usd_request.json(),
        'EUR': eur_request.json(),
        'BTC': btc_request.json()
    }

    return valores


def valores_agora() -> Dict:
    url_valores = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    valores_json = url_valores.json()

    valores = {
        'USD': valores_json["USDBRL"],
        'EUR': valores_json["EURBRL"],
        'BTC': valores_json["BTCBRL"]
    }

    return valores


valores_ontem = valores_ontem()
print(valores_ontem['USD'])
print(valores_ontem['BTC'])
print(valores_ontem['EUR'])

valores_agora = valores_agora()
print(valores_agora['USD'])
print(valores_agora['BTC'])
print(valores_agora['EUR'])

# while True:
# tabela = pd.read_excel("Cotações.xlsx")
# tabela.loc[0, "Cotação"] = float(cotacao_dolar)
# tabela.loc[1, "Cotação"] = float(cotacao_euro)
# tabela.loc[2, "Cotação"] = float(cotacao_btc) * 1000
# tabela.loc[0, "Data da Última Atualização"] = datetime.now()

# tabela.to_excel("Cotações.xlsx", index=False)

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


# noticias = 'UOL:\n'
# for i in ultimas_noticias_uol():
#     noticias += i+'\n\n'

# noticias += 'g1:\n'

# for i in ultimas_noticias_g1():
#     noticias += i+'\n\n'

# print(noticias)

# Significado regex [^>]* ==> aceita qualquer caractere diferente de '>' e o asterisco
# representa que a expressão anterior pode acontecer 0 ou infinitas vezes
# Significado regex (.*?) ==>
