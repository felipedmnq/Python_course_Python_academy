# HERANÇA

class Stack:

    # método inicializador da classe (construtor).
    def __init__(self):
        # cria atributo privado (imutável) "__".
        self.__stck = []


    # o self é o objeto em sí - no caso o "stck", um objt type list.
    def push(self, number):
        self.__stck.append(number)


    def pop(self):
        value = self.__stck[-1]
        del self.__stck[-1]
        return value


    #  função para mostrar a lista "stack".
    def show_stack(self):
        print(self.__stck)


# CRIAR UMA PILHA QUE CONTENHA UM "SOMADOR" E MANTENHA A SOMA DOS NÚMEROS NA PILHA.
class Stack_sum(Stack):
    def __init__(self):
        Stack.__init__(self)  # "chama a variável inicial da classe Stack.(a lista)
        # "__" mantém a variável privada --> é chamado de dunder - double underscore
        self.__sum = 0

    def get_sum(self):
        return self.__sum


    # sobrescrita das funções - push == + 1; pop == -1.
    def push(self, number):
        self.__sum += number
        Stack.push(self, number)


    def pop(self):
        value = Stack.pop(self)
        self.__sum -= value
        return value


stack = Stack_sum()
stack.push(10)
stack.push(15)
stack.push(19)
# não é possivel apenas mostrar a lista stock, pois é privado.
stack.show_stack()
print(stack.get_sum())
print(stack.pop())      # desempilhar.
print(stack.get_sum())
stack.show_stack()