"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""
import re

def not_bad(phrase):
    notpos, badpos = phrase.find('not'), phrase.find('bad')
    
    if badpos > notpos:
        substring_not_bad = phrase[notpos:badpos + 3]
        phrase = phrase.replace(substring_not_bad, 'good') 
    
    return phrase
    
def not_bad_two(phrase):
    not_, bad_ = phrase.find('not'), phrase.find('bad')
    
    if not_ < bad_:
        edge = phrase[bad_+3:] #if phrase[-1] in '?!.' else ''
        phrase = phrase[:not_] + 'good' + edge 

    return phrase
    
    
def regex_not_bad(phrase):
    pattern = r"not.*bad" 
    repl = r"good"
    return re.sub(pattern, repl, phrase)


def one_line_not_bad(phrase):
    return phrase if phrase.find('not') > phrase.find('bad') else phrase.replace(phrase[phrase.find('not'):phrase.find('bad') + 3], 'good')
    

def regex_one_line_not_bad(phrase):
    return re.sub(pattern='not.*bad', repl='good', string=phrase, flags=re.IGNORECASE) 


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
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
    test(not_bad, "It's notbad ok.", "It's good ok.")
    
    test(not_bad_two, 'This movie is not so bad', 'This movie is good')
    test(not_bad_two, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad_two, 'This tea is not hot', 'This tea is not hot')
    test(not_bad_two, "It's bad yet not", "It's bad yet not")
    test(not_bad_two, "It's not bad ok.", "It's good ok.")
    
    test(regex_not_bad, 'This movie is not so bad', 'This movie is good')
    test(regex_not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(regex_not_bad, 'This tea is not hot', 'This tea is not hot')
    test(regex_not_bad, "It's bad yet not", "It's bad yet not")
    test(regex_not_bad, "It's notbad ok.", "It's good ok.")
    
    test(one_line_not_bad, 'This movie is not so bad', 'This movie is good')
    test(one_line_not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(one_line_not_bad, 'This tea is not hot', 'This tea is not hot')
    test(one_line_not_bad, "It's bad yet not", "It's bad yet not")
    test(one_line_not_bad, "It's notbad ok.", "It's good ok.")
    
    test(regex_one_line_not_bad, 'This movie is not so bad', 'This movie is good')
    test(regex_one_line_not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(regex_one_line_not_bad, 'This tea is not hot', 'This tea is not hot')
    test(regex_one_line_not_bad, "It's bad yet not", "It's bad yet not")
    test(regex_one_line_not_bad, "It's notbad ok.", "It's good ok.")
    test(regex_one_line_not_bad, "It's Not bad ok.", "It's good ok.")
    test(regex_one_line_not_bad, "It's not bAd ok.", "It's good ok.")