import requests
import json 
import hashlib
from time import sleep

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
token = 'f57f9cd8513d5605b36309a307fb25c9ab3e8e9b'

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={0}'.format(token)
response = requests.get(url)
response_json = response.json()
numero_casas = response_json['numero_casas']
cifrado = response_json['cifrado']
resumo_criptografico = response_json['resumo_criptografico']

def decifra():
    msg = ''
    print('Mensagem cifrada:::::')
    print(cifrado)
    for x in cifrado:
        if x in alfabeto:
            posicao = alfabeto.index(x)
            msg = msg + alfabeto[posicao - numero_casas]
        else:
            msg = msg + x    
    print('Mensagem decifrada:::::')
    print(msg)
    return msg


documento = decifra()
r_criptografico = hashlib.sha1(str(documento).encode('utf-8')).hexdigest()

objeto = {
    'numero_casas': numero_casas,
    "token": token,
    "cifrado": cifrado,
    "decifrado": documento,
    "resumo_criptografico": r_criptografico,
}

def abre_json():
    arquivo = open('answer.json', 'w');
    json.dump(objeto, arquivo, indent=4, sort_keys=False)
    arquivo.close()

def post():
    url_post = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={0}'.format(token)
    file = {"answer": open("answer.json", "rb")}
    requests.post(url_post, files = file)
    print(response.status_code)