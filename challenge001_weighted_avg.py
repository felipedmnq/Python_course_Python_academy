'''
Desafio: Média Ponderada.
Leia 3 valores de ponto flutuante, um em cada linha. Depois, calcule a média ponderada desses valores.
O primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro tem peso 5.
Exemplo:
5.0
6.0
7.0
Saída:
6.3
'''

p1 = 2
p2 = 3
p3 = 5
val_a = float(input('Digite o 1º valor: ')) * p1
val_b = float(input('Digite o 2º valor: ')) * p2
val_c = float(input('Digite o 3º valor: ')) * p3

print(f'Média ponderada = {(val_a + val_b + val_c) / (p1 + p2 + p3)}.')



