import requests
import json

api_key = "your_key"

while True:
    entrada = str(input('Digite um nome de um filme ou "SAIR" para sair: ')).strip().lower()
    if entrada == "sair":
        break
    try:
        req = requests.get(f'https://www.omdbapi.com/?apikey={api_key}={entrada}' + '&type=movie')
    except Exception as e:
        print(f'Erro: {e}')
        continue
    else:
        try:
            dicionario = json.loads(req.text)
            print(f'Título : {dicionario["Title"]}\nAno    : {dicionario["Year"]}\nDiretor: {dicionario["Director"]}'
                  f'\nAtores : {dicionario["Actors"]}\nNota   : {dicionario["imdbRating"]}')
            print('━'*30)
            break
        except Exception as e:
            print(f'Erro: {e}')
            continue