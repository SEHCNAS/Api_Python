# Necessario instalar o requests
# tbm precisei rodar esse comando - include python to windows PATH variable,
# then run python -m ensurepip
from pip._vendor import requests
import json


def Buscar_Dados():
    request = requests.api.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL')
    resp = json.loads(request.content)
    return float(resp['USDBRL']['bid'])

print(Buscar_Dados())
