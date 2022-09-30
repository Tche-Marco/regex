from noticias import get_ultimas_noticias


def enviar_cotacao_e_noticias(valor_btc_atualizado) -> None:
    """Por enquanto, apenas imprime na tela o valor atualizado do BTC e as últimas notícias, mas o objetivo é mandar essas informações por email

    Args:
        valor_btc_atualizado (float): Valor atualizado do BTC
    """
    print(f'Valor do bitcoin atualizado: {valor_btc_atualizado}')
    print(get_ultimas_noticias())
