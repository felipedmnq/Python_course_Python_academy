import sys
def f_simples(b):
    b = 1/a


def outrafuncao(a):
    f_simples(a)


# Try/except/finally
# serve como um 'if' para erros.
try:
    a = int(input())
    outrafuncao(a)
    print('Tudo certo')
# esecuta o programa até encontrar erro, caso encontre pula para o exept.
#except:
except ZeroDivisionError:   # quando se sabe qual o erro especifico que pode ocorrer.
    print('Não é permitido divisão por ZERO.')
    print(sys.exc_info())
# o sys (inportado) mostra a classe do erro.
except ValueError:
    print('Use apenas números')
finally:
    print('Finally Sempre aparece')
# o finally sempre executa.
# com o TRY, o traceback não aparece, ele executa o programa "escondendo" o erro.

# o Try serve também para "prever" um possível erro do usuário e emitir
# uma mensagem sobre o erro. EX: 'Não é permitido divisão por ZERO.'
# usado muito para gerenciar os erros.