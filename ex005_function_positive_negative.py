'''
Crie uma função que reveba um número e rotorne P caso positivo ou N caso negativo.
'''


def positive_negative(n):
    '''
    If "n" is a positive number, return "P" (blue) or negative, return "AND" (red).
    :param n: "int" to be analyzed.
    :return: "P" (blue) if n == positive or "N" (red) if n == negative.
    '''
    if n > 0:
        ret = f'\033[1;34m{"P"}\033[m'
    else:
        ret = f'\033[1;31m{"N"}\033[m'
    return ret


print(positive_negative(4))
