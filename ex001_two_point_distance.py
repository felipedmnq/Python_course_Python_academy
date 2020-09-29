'''
Calcular a distância entre dois pontos A e B no plano cartesiano.
'''
from math import sqrt

x1 = int(input('Digite a coordenada "X" do ponto 1: '))
y1 = int(input('Digite a coordenada "Y" do ponto 1: '))
x2 = int(input('Digite a coordenada "X" do ponto 2: '))
y2 = int(input('Digite a coordenada "Y" do ponto 2: '))

distance = ((x1 - x2)**2) + ((y1 - y2)**2)
distance_ruth = sqrt(distance)

print(f'A distância entre o ponto A e B é igual a {distance_ruth:.2f}.')
