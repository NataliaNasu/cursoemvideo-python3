nome = str(input('Qual é o seu nome? '))

if nome == 'Natália':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome para meninas!')
else:
    print('Seu nome é bem normal...')
print(f'Tenha um bom dia, {nome}!')

'''Pode usar quantos elif's vc quiser, 
o único obrigatório é o if,
o else tb é opcional'''
'''else if = elif'''
'''Lembrar sempre do : após o if/elif/else'''