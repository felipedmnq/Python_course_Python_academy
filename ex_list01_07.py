'''
7) Faça um programa que converta a temperatura digitada em Celsius para Fahrenheit.
Cálculo para Fahrenheit: F = 9*C/5+32
'''

temp = float(input('Digite a temperatura em Cº: '))

fahrenheit = temp * (9 / 5) + 32
print(f'{temp}ºC = {fahrenheit:.2f}ºF')