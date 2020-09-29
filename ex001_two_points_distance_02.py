'''
Calcular a distância entre dois pontos A e B no plano cartesiano.
'''
# Read coordinates X and Y and keep in 2 variables.
x1, y1 = input('Digite as coordenadas de "X": ').split()
x2, y2 = input('Digite as coordenadas de "Y": ').split()
# change X and Y (str) to int().
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
#
from math import sqrt
distance = sqrt((x1-x2)**2 + (y1-y2)**2)
print(f'Distância = {distance:.2f}.')
