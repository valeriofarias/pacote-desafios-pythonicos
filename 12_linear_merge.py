"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

def linear_merge(list1, list2):
    list1_len, list2_len, olist = len(list1)-1, len(list2)-1, []

    if list1_len > list2_len:
        for i, j in enumerate(list1):
            if i <= list2_len:
                if list2[i] < list1[i]:
                    olist.append(list2[i])
                    olist.append(list1[i])
                else:
                    olist.append(list1[i])
                    olist.append(list2[i])
            else:
                olist.append(list1[i])
    
    elif list1_len < list2_len:
        for i, j in enumerate(list2):
            if i <= list1_len:
                if list2[i] < list1[i]:
                    olist.append(list2[i])
                    olist.append(list1[i])
                else:
                    olist.append(list1[i])
                    olist.append(list2[i])
		
            else:
               olist.append(list2[i])
            
    return olist
 
from heapq import merge  
def linear_merge_heapq(list1, list2):
    return list(merge(list1, list2))
    
    
# Inspirado por https://github.com/dougfraga/pythonic-challenges/blob/master/12_linear_merge.py
# Obs. Faço uma cópia de list1 e list2 para que sejam mostradas no teste, pois o pop deleta os itens.
# Obs2. Uso len(list1) + len(list2) pois é mais rápido que len(list1 + list2). Esse último é inclusive 
# uma concatenação das listas e perderia a regra do merge linear.
from collections import deque
def linear_merge_deque(list1, list2):
    list1_, list2_, olist = list1[:], list2[:], deque()
    while len(list1_) + len(list2_) > 0:
        if list1_[-1:] > list2_[-1:]:
            olist.appendleft(list1_.pop())
        else:
            olist.appendleft(list2_.pop())
    return list(olist)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

    test(linear_merge_heapq, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge_heapq, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge_heapq, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

    test(linear_merge_deque, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge_deque, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge_deque, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

