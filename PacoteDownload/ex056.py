#Ler o nome, idade e sexo de 4 pessoas.
#Ver a media da idade, nome do h mais velho.
#e, qntas mulheres abaixo de 20 anos.

soma = total = totalF = maior = 0
maisVelho = ''
for c in range(1, 5):
    nome = str(input(f"Digite o nome da {c}a pessoa: "))
    idade = int(input('Idade: '))
    sexo = str(input(f'Sexo: [F/M] '))
    soma += idade
    total += 1
    if sexo == 'M' or sexo == 'm': #sexo in 'Mm'
        if c == 1:
            maior = idade
            maisVelho = nome
        else:
            if maior < idade:
                maior = idade
                maisVelho = nome
    elif sexo == 'F' or sexo == 'f':
        if idade < 20:
            totalF += 1

media = soma / total
print(f'A média de idade é igual a {media:.1f} anos.')
print(f'O homem mais velho é o {maisVelho}, com {maior} anos.')
print(f'E, existe(m) {totalF} mulher(es) com menos de 20 anos.')