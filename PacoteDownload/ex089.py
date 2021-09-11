# leia o nome e 2 notas de vários alunos.
# mostre o boletim com a média de cada um e, permita que o usário,
# possa mostrar as notas de cada alunos individualmente.
alunos = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    opcao = input('Deseja continuar? [S/N] ').upper()
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N] ')
    if opcao == 'N':
        break
