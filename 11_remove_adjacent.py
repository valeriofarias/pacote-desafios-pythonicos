"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    listn = [nums[0]] if nums else []
    for i, j in enumerate(nums):
        if nums[i] != listn[-1]:
            listn.append(nums[i])   
    return listn
    
    
def remove_adjacent_using_del(nums):
    len_nums, i = len(nums), 0
    while i < len_nums - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
            len_nums = len(nums)
        else:
            i += 1
    return nums
    

def remove_adjacent_using_zip(nums):
    listn = [nums[0]] if nums else []
    for i, j in zip(nums, nums[1:]):
        if i != j:
            listn.append(j)
    return listn
   

def remove_adjacent_one_line(nums):
    return [i for i, j in zip(nums, nums[1:]+[None]) if i != j]


from itertools import groupby
def remove_adjacent_groupby(nums):
    return [i for i, j in groupby(nums)]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
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


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    
    test(remove_adjacent_using_del, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent_using_del, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent_using_del, [], [])
    test(remove_adjacent_using_del, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    

    test(remove_adjacent_using_zip, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent_using_zip, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent_using_zip, [], [])
    test(remove_adjacent_using_zip, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    
    test(remove_adjacent_one_line, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent_one_line, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent_one_line, [], [])
    test(remove_adjacent_one_line, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])

    test(remove_adjacent_groupby, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent_groupby, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent_groupby, [], [])
    test(remove_adjacent_groupby, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])