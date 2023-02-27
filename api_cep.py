import pandas as pd
import requests 
import os
from zipfile import ZipFile

os.system('cls')

cep = input('Digite seu CEP: ')
r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

data = r.json()

print('CEP: {}'.format(data['cep']))
print('logradouro: {}'.format(data['logradouro']))
print('complemento: {}'.format(data['complemento']))
print('bairro: {}'.format(data['bairro']))
print('localidade: {}'.format(data['localidade']))
print('uf: {}'.format(data['uf']))
print('ddd: {}'.format(data['ddd']))


