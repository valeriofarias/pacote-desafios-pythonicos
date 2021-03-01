"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
import math

def front_back(a, b):
    abegin = a[:int(len(a)/2)] if len(a) % 2 == 0 else a[:int(len(a)/2)+1]
    aend = a[int(len(a)/2):] if len(a) % 2 == 0 else a[int(len(a)/2)+1:]

    bbegin = b[:int(len(b)/2)] if len(b) % 2 == 0 else b[:int(len(b)/2)+1]
    bend  = b[int(len(b)/2):] if len(b) % 2 == 0 else b[int(len(b)/2)+1:]

    return abegin + bbegin + aend + bend
    
    
def front_back_two(a, b):
    def begins(s):
        return s[:int(len(s)/2)] if len(s) % 2 == 0 else s[:int(len(s)/2)+1]

    def ends(s):
        return s[int(len(s)/2):] if len(s) % 2 == 0 else s[int(len(s)/2)+1:]

    return ''.join([begins(a), begins(b), ends(a), ends(b)])


# --- Solução mais expressiva 
    
def front_back_using_ceil(a, b):
    def index(s):
        return math.ceil(len(s)/2)

    def begins(s):
        return s[:index(s)] 

    def ends(s):
        return s[index(s):] 

    return f'{begins(a)}{begins(b)}{ends(a)}{ends(b)}'


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
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')

    test(front_back_two, ('abcd', 'xy'), 'abxcdy')
    test(front_back_two, ('abcde', 'xyz'), 'abcxydez')
    test(front_back_two, ('Kitten', 'Donut'), 'KitDontenut')
    
    test(front_back_using_ceil, ('abcd', 'xy'), 'abxcdy')
    test(front_back_using_ceil, ('abcde', 'xyz'), 'abcxydez')
    test(front_back_using_ceil, ('Kitten', 'Donut'), 'KitDontenut')
