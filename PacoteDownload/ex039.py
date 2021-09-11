from datetime import date
anoNasc = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year #Qual o ano de hoje?
idade = ano - anoNasc
print(f'Você tem {idade} anos.')
if idade < 18:
    faltam = 18 - idade
    print(f'E, falta {faltam} anos, para você se alistar!')
elif idade == 18:
    print('E, está na idade de se alistar!')
else:
    passou = idade - 18
    print(f'E, espero que já tenha se alistado.'
          f'\nCaso contrário, está {passou} anos atrasado.')
