'''
1) Faça um programa que leia dois números e calcule:
a) A soma.
b) A subtração.
c) A multiplicação.
d) A divisão.
e) A exponenciação.
f) O módulo.
g) O resto.
'''

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

print(f'{n1} + {n2} = {n1 + n2}.'
      f'\n{n1} - {n2} = {n1 - n2}.'
      f'\n{n1} X {n2} = {n1 * n2}.'
      f'\n{n1} / {n2} = {n1 / n2}.'
      f'\n{n1} ^ {n2} = {n1 ** n2}.'
      f'\n{n1} // {n2} = {n1 // n2}.'
      f'\n{n1} % {n2} = {n1 % n2}.')