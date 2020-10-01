# definir classe:

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


stack = Stack()
stack.push(10)
stack.push(15)
stack.push(19)
# não é possivel apenas mostrar a lista stock, pois é privado.
stack.show_stack()
print(stack.pop())      # desempilhar.
stack.show_stack()
