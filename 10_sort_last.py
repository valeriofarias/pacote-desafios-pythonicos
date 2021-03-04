"""
10. sort_last

Dada uma lista de tuplas não vazias, retorne uma lista ordenada em ordem
crescente com base no último elemento de cada tupla.

Exemplo: [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
Irá retornar: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

Dica: Use uma custom key= function para extrair o ultimo elemento de cada tupla.

1. Desafio extra: criar o próprio algoritmo de programação e em seguida verificar 
em que ponto do algoritmo pode ser simplificado com funções que muda o comportamento
da lógica. 

2. Pode ser por função anônima (lambda), definir uma função que fará o papel de chave
e passar para o key e é possível procurar na biblioteca padrão do python a função
getitem que faz parte do repertório de programação funcional da linguagem e vai 
ajudar a resolver o problema com pouquìssimo esforço. 
"""
def sort_last(tuples):
    return sorted(tuples, key=lambda x : x[-1])
   
    
def sort_last_with_funcion(tuples):
    def getkey(item):
        return item[-1]
          
    return sorted(tuples, key=getkey)
    
    
from operator import itemgetter
def sort_last_get_item(tuples):
    return sorted(tuples, key=itemgetter(-1))
    

# https://www.codeproject.com/articles/1112298/the-simplest-sorting-algorithm-example-why-would-s    
# Bubble sort is one of the worst sort algorithm in performance but it is the best in didatic, it's simple to underestand.
# The function bellow is only an example to figure out how bubble sort works.
def bubble_sort_algorithm(lista):
    for item in range(1, len(lista)):
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista

# Use key = -1 to order by the last item in the tuple
def bubble_sort(lista, key=0):
    for item in range(1, len(lista)):
        for i in range(0, len(lista)-1):
            if type(lista[i]) == int or type(lista[i]) == str:
                if lista[i] > lista[i+1]:
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp
            elif type(lista[i]) == list or type(lista[i]) == tuple:
                if lista[i][key] > lista[i+1][key]:
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp        
    return lista


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """on
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


def test_two_parameters(f, in_, in2_, expected):
    """on
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_, in2_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r},{in2_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(sort_last, [(1, 3), (3, 2), (2, 1)],
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last, [(2, 3), (1, 2), (3, 1)],
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


    test(sort_last_with_funcion, [(1, 3), (3, 2), (2, 1)],
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last_with_funcion, [(2, 3), (1, 2), (3, 1)],
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last_with_funcion, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
         
    test(sort_last_get_item, [(1, 3), (3, 2), (2, 1)],
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last_get_item, [(2, 3), (1, 2), (3, 1)],
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last_get_item, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
         
    test(bubble_sort_algorithm, [15, 4, 1, 29, 107, 56, 11, 22],   
         [1, 4, 11, 15, 22, 29, 56, 107])
         
    test(bubble_sort, [15, 4, 1, 29, 107, 56, 11, 22],   
         [1, 4, 11, 15, 22, 29, 56, 107])
    test(bubble_sort, ['z', 'f', 'c', 'o', 'd', 'k', 'x','e'],   
         ['c', 'd', 'e', 'f', 'k', 'o', 'x', 'z'])
    test(bubble_sort, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(1, 7), (1, 3), (2, 2), (3, 4, 5)])     
    test_two_parameters(bubble_sort, [(1, 7), (1, 3), (3, 4, 5), (2, 2)], -1,
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
