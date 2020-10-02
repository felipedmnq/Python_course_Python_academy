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

print('-' * 30)
# ANEXAR DADOS AO ARQUIVO
# "w" escreve no arquivo apagando o texto antigo.
file = open('teste.txt', 'w')
file.write('Ola Felipe')        # write para estrever no arquivo.txt
file.write('\nesse texto aparece e substitui o anterior quando "W" eh o modo.')
# "\n" quebra linha.

# para ler o arquivo novamente.
file = open('teste.txt', 'r')
print(file.read())

# "a" == .append --> vai anexando a informação ao final do texto
# a cada execução.
file = open('teste.txt', 'a')
file.write('\nesse texto apare e eh repitido quando "A" é o modo.')
# cada vez que eu executo o comando, ele escreve novamente no arquivo.
# fica salvo.

# quando o modo é "W" (write), deve-se sempre "fechar" o arquivo.
# regra geral - quando se abre um arquivo para escrita, o sistema bloqueia
# o acesso a outros usuários para escrita, por isso deve-se fechar o arquivo.

#FECHAR ARQUIVO.
file.close()  # encerra o objeto file.

# abrir arquivo para "create" -- "X".
file = open('new_file.txt', 'x')  # novo arquivo criado
file.write('Novo arquivo criado')
file.close()

# ler o novo arquivo.
file = open('new_file.txt', 'r')
print(file.read())




