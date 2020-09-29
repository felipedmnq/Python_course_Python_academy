'''
9) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário
e a porcentagem de aumento. Mostre o valor do aumento e do novo salário.
'''

salary = float(input('Sarário: R$ '))
rise = int(input('Porcentagem de aumento (%): '))

print(f'Salário corrigido: R$ {salary * ((rise / 100) + 1):.2f}')
