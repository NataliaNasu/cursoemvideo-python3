from datetime import date
anoNasc = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - anoNasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')