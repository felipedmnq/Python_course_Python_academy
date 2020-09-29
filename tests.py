squares_pair = []
for i in range(1, 51):
    if i % 2 == 0:
        squares_pair.append(i ** 2)

print(squares_pair)

squares_pair02 = [i ** 2 for i in range(1, 51) if i % 2 == 0]
print(squares_pair02)