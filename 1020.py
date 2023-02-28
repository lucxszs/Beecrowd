import os

os.system('cls')

dia = int(input())

ano = dia // 365
dia = dia % 365

mes = dia // 30
dia = dia % 30

print(ano,'ano(s)') 
print(mes,'mes(es)')
print(dia,'dia(s)')






















