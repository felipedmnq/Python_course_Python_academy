'''
2) Faça um programa que peça 4 notas bimestrais e mostre a média.
'''

n1 = float(input('Digite a nota do 1º semestre: '))
n2 = float(input('Digite a nota do 2º semestre: '))
n3 = float(input('Digite a nota do 3º semestre: '))
n4 = float(input('Digite a nota do 4º semestre: '))
avg = (n1 + n2 + n3 + n4) / 4

print(f'A média do aluno foi: {avg:.2f}.')