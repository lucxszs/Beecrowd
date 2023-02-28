import os

os.system('cls')

n = int(input())

horas = n // 3600
segundos = n % 3600

minutos = segundos // 60
segundos = segundos % 60


print(f'{horas}:{minutos}:{segundos}')