# exemplo de paradgma procedural.
'''
Implementar uma estrutura de dados denominada "PILHA".
'''

stack = []


def stack_up(stack_int, number):
    '''
    Adiciona um elemento ao topo da pilha (push)
    :param number:
    :return:
    '''
    # o final da lista é o topo da pilha.
    stack.append(number)


def unstack(stack_int):
    '''
    Desempilhar (pop) retira um elemento do topo da pilha e retorna seu valor.
    :param number:
    :return:
    '''
    value = stack_int[-1]
    del stack_int[-1]
    return value


stack_up(stack, 10)
stack_up(stack, 17)
stack_up(stack, 20)


print(stack)


print(unstack(stack))
print(stack)