import time

from emails import enviar_cotacao_e_noticias
from valores_atualizados import get_valor_btc_atual, get_maior_e_menor_valor_btc_ontem


min_valor_btc_ontem, max_valor_btc_ontem = get_maior_e_menor_valor_btc_ontem()
# min_valor_btc_ontem = float(105)  # USAR P/ TESTES
# max_valor_btc_ontem = float(90.91) # USAR P/ TESTES
print(f"Menor valor BTC ontem: {min_valor_btc_ontem}")
print(f"Maior valor BTC ontem: {max_valor_btc_ontem}")


def verifica_alteracao_btc(valor_btc_atualizado) -> dict:
    """Verifica se houve variação de valor do bitcoin comparando o valor atual com o das mínimas e máximas de ontem

    Args:
        valor_btc_atualizado (float): Valor atualizado do bitcoin (última atualização)

    Returns:
        dict: Dicionário contendo o status e a porcentagem da variação de valor do bitcoin  
    """

    retorno = {
        "porcentagem": 0,
        "status": "Manteve"
    }

    if valor_btc_atualizado > max_valor_btc_ontem:
        variacao = valor_btc_atualizado - max_valor_btc_ontem
        porcentagem = (variacao * 100) / max_valor_btc_ontem

        retorno = {
            "porcentagem": porcentagem,
            "status": "Aumento"
        }

    elif valor_btc_atualizado < min_valor_btc_ontem:
        variacao = min_valor_btc_ontem - valor_btc_atualizado
        porcentagem = (variacao * 100) / min_valor_btc_ontem

        retorno = {
            "porcentagem": porcentagem,
            "status": "Queda"
        }

    return retorno


def verifica_valor_btc():
    """Verifica em tempo real (looping infinito) se houve variação no valor do bitcoin levando em consideração as máximas e mínimas do bitcoin de ontem e, caso haja uma variação considerável, "envia" um aviso informando qual foi a variação do valor e as últimas notícias do G1 e UOL
    """

    while True:
        valor_btc_atualizado = get_valor_btc_atual()
        print(f"Valor BTC atualizado: {valor_btc_atualizado}")

        alteracao_bitcoin = verifica_alteracao_btc(valor_btc_atualizado)

        if alteracao_bitcoin["porcentagem"] > 0.02:

            if alteracao_bitcoin["status"] == "Aumento":
                print(
                    "Comparado à máxima de ontem ({}), o valor do bitcoin aumentou {}%".format(
                        max_valor_btc_ontem,
                        alteracao_bitcoin["porcentagem"]
                    )
                )
                enviar_cotacao_e_noticias(valor_btc_atualizado)

            elif alteracao_bitcoin["status"] == "Queda":
                print(
                    "Comparado à mínima de ontem ({}), o valor do bitcoin diminuiu {}%".format(
                        min_valor_btc_ontem,
                        alteracao_bitcoin["porcentagem"]
                    )
                )
                enviar_cotacao_e_noticias(valor_btc_atualizado)

        time.sleep(2)


verifica_valor_btc()
