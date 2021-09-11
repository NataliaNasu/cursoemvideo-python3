#leia vários números inteiros.
#mostre a média e, ql foi o maior e o menor.
#deve pergunta se deseja inserir outros numeros ou nao.

soma = total = maior = menor = 0
r = ''
while r != 'N': #while r in 'Ss'
    n = int(input('Digite um número: '))
    soma += n
    if total == 0:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    total += 1
    r = str(input('Deseja continuar? [S/N] ')).upper()

media = soma / total
print(f'A media entre os {total} números = {media:.2f}.')
print(f'E, o maior número foi {maior} e o menor, {menor}.')
