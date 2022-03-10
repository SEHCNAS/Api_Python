# Necessario instalar o requests
# tbm precisei rodar esse comando - include python to windows PATH variable,
# then run python -m ensurepip
# doc api - https://docs.awesomeapi.com.br/api-de-moedas
from pip._vendor import requests
import json


def Buscar_Dados():
    # Url com o parametro da moeda fixo
    request = requests.api.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL')
    # pega o retorno e joga em um json
    resp = json.loads(request.content)
    # Retorna so somente um item do json - resp['USDBRL']['bid']
    # Retorna o json inteiro - resp['USDBRL']['bid']
    return resp['USDBRL']['bid']

print(Buscar_Dados())
