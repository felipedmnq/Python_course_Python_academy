# ARQUIVOS --> TEXTO OU BINÁRIOS

# OPEN()

file = open('teste.txt', 'r')

# READ()
# lê o arquivo.
print(file.read())

# lê os caracteres determinados dentro do arquivo, x caracteres.
file = open('teste.txt', 'r')
print(file.read(4))  # --> "ola_"

# lê uma linha do arquivo - cada vez que coloca, lê uma das palavras.
file = open('teste.txt', 'r')
print(file.readline())

# o número dentro dos parenteses mostra a quantidade de caracteres que serão lidos.
file = open('teste.txt', 'r')
print(file.readline(2))     # --> "ol"
print(file.readline(2))     # --> "a_"
print(file.readline(3))     # --> "mun"

# lê o arquivo em forma de lista, dentro dos parenteses fica o índice.
file = open('teste.txt', 'r')
print(file.readlines())  # --> ['ola\n', 'mundo\n', 'ola mundo']

# lê o numero de caracteres dentro do parênteses.
file = open('teste.txt', 'r')
print(file.readlines(5))  # --> ['ola\n', 'mundo\n']; 5 está em "mundo"

file = open('teste.txt', 'r')
for line in file:
    line = line.replace('\n', '') # --> funciona como o (end='')
    #print(line, end='')
    print(line)