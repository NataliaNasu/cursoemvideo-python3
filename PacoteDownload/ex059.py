#leia dois números e mostre um menu com as operações.
# faça-os até parar
from time import sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Segundo número: '))

opcao = 0
while opcao != 5:
    print('OPERAÇAÕES:'
          '\n[1] somar'
          '\n[2] multiplicar'
          '\n[3] maior'
          '\n[4] novos números'
          '\n[5] sair do programa')
    opcao = int(input('Qual a sua escolha? '))
    if opcao == 1:
        soma = n1 + n2
        print(f"SOMA: {n1} + {n2} = {soma}")
        sleep(2)
    elif opcao == 2:
        multi = n1 * n2
        print(f'MULTIPLICAÇÃO: {n1} x {n2} = {multi}')
        sleep(2)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}:'
              f'\nO MAIOR é {maior}')
        sleep(2)
    elif opcao == 4:
        print('Digite novos valores: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        break
    else:
        print('Opção inválida... Tente outra vez!')
print('FIM DO PROGRAMA! Volte sempre^^')