import requests
import re


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


def get_ultimas_noticias():
    noticias = {
        'g1': ultimas_noticias_g1(),
        'uol': ultimas_noticias_uol()
    }
    return noticias
