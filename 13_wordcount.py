"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
from itertools import groupby

def report(words):
    return '\n'.join([f'{w} {qty}' for w, qty in words])

def open_file(filename):
    with open(filename) as file_object:
        return file_object.read()

        
def split_text(text):
    return text.split()

    
def lower_words(list):
    return [str.lower(i) for i in list]

    
def wordcount(wordlist):
    return {w:len(list(qty)) for w, qty in groupby(wordlist)}


def print_words(filename):
    wordlist = sorted(lower_words(split_text(open_file(filename))))
    wordcountdict = wordcount(wordlist)  
    return report(wordcountdict.items())


def print_top(filename):
    wordlist = lower_words(split_text(open_file(filename)))
    wordcountdict_top20 = dict(sorted(wordcount(wordlist).items() , reverse=True, key=lambda x: x[1])[:20])
    return report(wordcountdict_top20.items())


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print(print_words(filename))
    elif option == '--topcount':
        print(print_top(filename))
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
