'''
Desafio
Serão dados 3 números inteiros, todos na mesma linha. Imprima na tela os números em ordem crescente, um em cada linha.
Exemplo:
​7 21 3
Saída
3
7
21
'''

num1, num2, num3 = (input("Digite 3 números inteiros separados por espaço: ")).split(' ')
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 < num2 and num1 < num3:
    print(num1)
    if num2 < num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 < num1 and num2 < num3:
    print(num2)
    if num1 < num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 < num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

