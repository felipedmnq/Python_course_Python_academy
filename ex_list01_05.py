'''
5) Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno,
sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
'''

n1 = float(input('Digite a nota do 1º semestre: ')) * 2
n2 = float(input('Digite a nota do 2º semestre: ')) * 3
n3 = float(input('Digite a nota do 3º semestre: ')) * 5

avg_pond = (n1 + n2 + n3) / 10
print(f'A média do aluno é: {avg_pond}.')