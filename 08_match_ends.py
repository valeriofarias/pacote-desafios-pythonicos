"""
08. match_ends

Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""

def match_ends(words):
    n = 0
    for word in words:
        n += 1 if len(word) > 1 and word[0] == word[-1] else 0

    return n    


def match_ends_list_comprehension(words):
    return len([word for word in words if len(word) > 1 and word[0] == word[-1]]) 



def match_ends_generator(words):
    return sum((1 for word in words if len(word) > 1 and word[0] == word[-1]))
    

import re
def match_ends_regex(words):
    phrase = '\n'.join(words)
    match = re.findall(pattern = r'^(.).*\1$',string = phrase, flags=re.MULTILINE)
    return len(match)      


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
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)

    test(match_ends_list_comprehension, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends_list_comprehension, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends_list_comprehension, ['aaa', 'be', 'abc', 'hello'], 1)
    
    test(match_ends_generator, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends_generator, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends_generator, ['aaa', 'be', 'abc', 'hello'], 1)

    test(match_ends_regex, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends_regex, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends_regex, ['aaa', 'be', 'abc', 'hello'], 1)
