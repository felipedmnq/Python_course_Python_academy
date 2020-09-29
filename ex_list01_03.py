'''
3) Faça um programa que peça 2 números inteiros e 1 número real. Calcule e mostre:
a) O produto do dobro do primeiro com metade do segundo.
b) A soma do triplo do primeiro com o terceiro.
c) O terceiro elevado ao cubo.
'''

n1 = int(input('Digite o um número inteiro: '))
n2 = int(input('Digite o outro número inteiro: '))
n3 = float(input('Digite o um número real: '))

a = (n1 * 2) * (n2 / 2)
b = (n1 * 3) + n3
c = n3 ** 3
print(f'{a}.\n{b}.\n{c}.')