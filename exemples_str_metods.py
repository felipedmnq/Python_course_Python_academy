nome = 'felipe'
nome.capitalize() # Coloca a primeira letra capitalizada.

nome_composto = 'felipe demenech vasconcelos'
nome_composto.title() # capitaliza todas as primeiras letras.

nome_maiusculo = 'FELIPE DEMENECH'
nome_maiusculo.casefold()  # todas as letras minúsculas, funciona para varios alfabetos.

nome_maiusculo.lower()  # todas minúsculas, funciona melhor para alfabeto normal.

nome_maiusculo.upper()  # todas as letras para maiúsculo.

# PADRÃO "IS".
# responde "perguntas" feitas para a string.

nome_composto.islower()     # são minusculos?
nome_maiusculo.isalpha()    # são alfabeticos?

# JOIN.

print(nome.join(nome_maiusculo))    # "junta" uma string na outra sendo a primeira entre
                                    # as letras separadas da segunda. EX: FfelipeEfelipeLfelipe...

str = 'felipe'
lstr = list(str)        # --> ['f', 'e', 'l', 'i', 'p', 'e']
print(''.join(lstr))    # --> felipe