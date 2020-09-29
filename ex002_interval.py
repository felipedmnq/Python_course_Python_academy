'''
ler numero inteiro e verificar em qual intervalo que se encontra o número digitado.
'''

num = int(input('Digite um valor: '))

if 0 <= num <= 50:
    print(f'{num} encontra-se no intervalo [0, 50].')
elif 50 < num <= 100:
    print(f'{num} encontra-se no intervalo [51, 100].')
else:
    print((f'{num} encontra-se fora do intervalo [0, 100].'))