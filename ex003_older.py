'''
ler nome e idade de duas pessoas e imprimir o nome do mais velho
'''

name01 = input('NOME 1ª PESSOA: ')
age01 = int(input('IDADE 1ª PESSOA: '))
name02 = input('NOME 2ª PESSOA: ')
age02 = int(input('IDADE 2ª PESSOA: '))

if age01 > age02:
    print(f'{name01} é o mais velho.')
else:
    print(f'{name02} é o mais velho.')