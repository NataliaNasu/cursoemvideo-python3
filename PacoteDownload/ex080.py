#leia 5 valores e coloque-os em ordem durante a inserção. mostre o final.

numero = []

for v in range(0, 5):
    n = int(input('Digite um valor: '))
    if v == 0:
        numero.append(n)
    elif n > numero[len(numero)-1]: #numero[-1] último elemento
        numero.append(n)
    else:
        posicao = 0
        while posicao < len(numero):
            if n <= numero[posicao]:
                numero.insert(posicao, n)
                break
            posicao += 1
print(numero)
