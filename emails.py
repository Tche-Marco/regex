from noticias import get_ultimas_noticias


def enviar_cotacao_e_noticias(valor_dolar_atualizado):
    print(f'Valor do dólar atualizado: {valor_dolar_atualizado}')

    get_ultimas_noticias()
    print(get_ultimas_noticias())
