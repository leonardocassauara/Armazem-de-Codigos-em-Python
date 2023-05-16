# Programa que usa o requests para pegar informações da cotação do dólar, usando uma API ou o RE para filtrar a informação da página ‘web’ e então mostrá-la
import requests

try:
    req = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/5?formato=json')
except Exception as e:
    print(f'Erro: {e}')
else:
    print('{:━^40}'.format(' Dólar - Últimos 5 dias '))
    data = req.json()
    for item in data:
        dia = item["data"]
        cotação = item["valor"]
        print(f'Data: {dia}, Cotação: \033[32m{cotação[:4]}\033[m')
    print('━'*40)