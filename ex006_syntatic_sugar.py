# List Comprehension.
# Syntatic Sugar.

squares = []

for i in range(1, 51):
    squares.append(i ** 2)

print(squares)

# Versão simplificada - Syntatic Sugar.
squares02 = [i ** 2 for i in range(1, 51)]   # nessa configuração pode-se   colocar qualquer tipode coisa na
                                             # lista diretamente, inclusive funcões.
print(squares02)


squares_pair = []
for i in range(1, 51):
    if i % 2 == 0:
        squares_pair.append(i ** 2)

print(squares_pair)

# Syntatic sugar
squares_pair02 = [i ** 2 for i in range(1, 51) if i % 2 == 0]
print(squares_pair02)

squares_pair03 = [i ** 2 for i in range(1, 51) if i % 2 == 0 if i < 20]
print(squares_pair03)
