import emails
import time
from valor_atualizado import get_valor_dolar_atual


valor_inicial_dolar_hoje = get_valor_dolar_atual()


def verifica_alteracao_dolar(valor_inicial_dolar_hoje, valor_dolar_atualizado):
    if valor_dolar_atualizado > valor_inicial_dolar_hoje:
        variacao = valor_dolar_atualizado - valor_inicial_dolar_hoje
        porcentagem = (variacao * 100) / valor_inicial_dolar_hoje
        return porcentagem

    elif valor_dolar_atualizado < valor_inicial_dolar_hoje:
        variacao = valor_inicial_dolar_hoje - valor_dolar_atualizado
        porcentagem = (variacao * 100) / valor_inicial_dolar_hoje
        return porcentagem
    return -1


def verifica_valor_dolar():
    while True:
        valor_dolar_atualizado = get_valor_dolar_atual()

        if verifica_alteracao_dolar(valor_inicial_dolar_hoje, valor_dolar_atualizado) > 0:
            emails.enviar_cotacao_e_noticias(valor_dolar_atualizado)

        time.sleep(2)


verifica_valor_dolar()
