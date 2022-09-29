from msilib.schema import Error
import requests
import re


def get_valor_dolar_atual():
    response = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL"
    )

    if response.status_code == 200:
        valor_dolar = response.json()
        return float(valor_dolar["USDBRL"]["bid"])

    raise Exception(
        "Ocorreu um erro inesperado!!! Status Code: {}".format(
            response.status_code)
    )
