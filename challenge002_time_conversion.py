'''
​Desafio:
​Dado um valor de tempo em segundos (inteiro), converta-o para o formato horas:minutos:segundos.
Exemplo:
556
Saída
0:9:16
'''

time = int(input('Digite quantos segundos deseja converter: '))
hour = time // 3600
min = (time % 3600) // 60
sec = time % 60

print(f'{hour}:{min}:{sec}')
