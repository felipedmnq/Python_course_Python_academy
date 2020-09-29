'''
10) Faça um programa que leia a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.
'''

days = int(input('Dias: '))
while True:
    hours = int(input('Horas: '))
    if hours < 24:
        break
    else:
        print('Hora inválida!')
while True:
    min = int(input('Minutos: '))
    if min < 60:
        break
    else:
        print('Valor inválido!')
while True:
    sec = int(input('Segundos: '))
    if sec < 60:
        break
    else:
        print('Valor inválido!')


sec_days = days * 86400
sec_hours = hours * 3600
sec_min = min * 60

print(f'{days}d:{hours}h:{min}m:{sec}s = {sec_days + sec_hours + sec_min + sec} segundos.')