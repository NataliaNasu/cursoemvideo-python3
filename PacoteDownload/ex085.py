#leia 7 numeros e cadastre-os em uma lista, separando os pares e ímpares.
#no final, mostre os valores pares e ímpares em ordem crescente

numero = []
par = []
impar = []
for i in range(0, 5):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
numero.append(par)
numero.append(impar)
print(numero)
par.sort()
impar.sort()
print(par)
print(impar)