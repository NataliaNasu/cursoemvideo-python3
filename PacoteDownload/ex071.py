#caixa eletronico. leia o valor de saque (inteiro)
#retorna qntas cédulas de cada valor serão entregues.
#cedulas = 50, 20, 10 e 1

saque = int(input('Digite o valor do saque: R$'))
cinq = vinte = dez = um = resto = 0

while True:
    cinq = saque // 50
    resto = saque % 50
    vinte = resto // 20
    resto = resto % 20
    dez = resto // 10
    resto = resto % 10
    um = resto // 1
    break
print(f'O valor de R${saque:.2f} será entregue da seguinte maneira:')
print(f'{cinq} cédulas de R$50.')
print(f'{vinte} cédulas de R$20')
print(f'{dez} cédulas de R$10')
print(f'{um} cédulas de R$1')