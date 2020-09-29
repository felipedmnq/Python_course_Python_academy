lista = []
n = int(input())
for i in range(n):
    num = int(input())
    lista.append(num)
print(f'Números digitados: {lista}.')
print(f'Média dos números digitados: {sum(lista) / n}.')

