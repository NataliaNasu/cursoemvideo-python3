'''Padrão ANSI = normalização internacional,
e tem escape sequence, que funciona em vários ambientes,
e será usado no terminal -> \ e o código'''

'''Em todo começo, se utiliza a \033[-codigo-m.
entre a [ e o m, pd ser atribuido um código, dois ou três.
o 1º é o estilo da fonte, o 2º a cor do texto e, 
por fim a cor do background
ex: \033[0;33;44m'''

'''CODIGOS INICIANTES:
Estilo da fonte: 
0 = none
1 = bold
4 = underline
7 = negative
-----------------
Cor do Texto:
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = roxo
36 = verde água
37 = cinza
*não tem código p preto, 
mas da pra gerar ela
-----------------
Cor de Fundo:
40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = roxo
46 = ciano
47 = cinza
'''

'''
letra branca e fundo preto é o padrão então, 
preto = \033[m -> "volta p padrão, desfaz as operações"

letra preta e fundo branco é o contrário de preto,
então, no estilo, se usa o 7 para inverter a cor 
da letra branca em preta = \033[7; 30m
'''
print('\033[0;30;41mOlá, Mundo!')
'''pra tirar a faixa de fundo completa = coloca no final \033[m'''

print('\033[0;30;41mOlá, Mundo!\033[m')
print('\033[30mOlá, mundo!') #letra branca, com fundo padrão = cinza
print('\033[37mOlá, mundo!')
print('\033[mOlá, mundo!')
print('\033[7;40mOlá, mundo!\033[m')
print('\033[7;37mOlá, mundo!\033[m')
print('\033[7;30mOlá, mundo!\033[m')

a = 3
b = 5
print(f'Os valores de a e b, são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')
nome = 'Natália'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;37m'}
print(f"Olá, Muito prazer, {cores['pretoebranco']}{nome}{cores['limpa']}!!!")
