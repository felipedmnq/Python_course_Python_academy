'''
4) Leia 2 valores de ponto flutuante A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno,
sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5.
'''

n1 = float(input('Digite a nota do 1º semestre: ')) * 3.5
n2 = float(input('Digite a nota do 2º semestre: ')) * 7.5

avg_pond = (n1 + n2) / (3.5 + 7.5)
print(f'A média do aluno foi: {avg_pond:.2f}.')