# Pré requisitos

```
Python == 3.10
```

Crie e habilite um ambiente python
```console
  python -m venv venv
```
```console
  venv\Scripts\activate | windows
  . venv/bin/activate | linux e macOs
```

Instale as dependências do projeto
```console
  pip install -r requirements.txt
```

# Inicialização
Execute o arquivo main
```console
  py main.py
```

# Funcionamento do App

```
Verifica, em tempo real, se houve variação no valor do bitcoin, levando em consideração as máximas e mínimas de ontem. Caso 
haja uma variação considerável, envia um aviso informando qual foi a variação do valor e as últimas notícias do G1 e UOL
```
