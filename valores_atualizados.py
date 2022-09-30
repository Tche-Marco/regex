import requests


def get_maior_e_menor_valor_btc_ontem() -> list:
    """Retorna a mínima e máxima do valor do bitcoin ontem

    Returns:
        list: Lista com a mínima e máxima do bitcoin ontem, respectivamente
    """

    response = requests.get(
        "https://economia.awesomeapi.com.br/json/daily/BTC-BRL/2"
    )

    if response.status_code == 200:
        valor_btc = response.json()
        return [float(valor_btc[1]["low"]), float(valor_btc[1]["high"])]

    raise Exception(
        "Ocorreu um erro inesperado!!! Status Code: {}".format(
            response.status_code)
    )


def get_valor_btc_atual() -> float:
    """Retorna o valor de compra atualizado do bitcoin

    Returns:
        float: Valor de compra atualizado do bitcoin
    """

    response = requests.get(
        "https://economia.awesomeapi.com.br/last/BTC-BRL"
    )

    if response.status_code == 200:
        valor_btc = response.json()
        return float(valor_btc["BTCBRL"]["bid"])

    raise Exception(
        "Ocorreu um erro inesperado!!! Status Code: {}".format(
            response.status_code)
    )
