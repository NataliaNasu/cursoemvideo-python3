#aprovação do empréstimo bancário
casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

parcelaMínima = salario * 30 / 100
prestacao = casa / (anos * 12)
print(f"Para pagar um casa de R${casa:.2f} em {anos} anos,"
      f"\nA prestação mínima deve ser de R${prestacao:.2f} reais.")

if prestacao > parcelaMínima:
    print('Empréstimo NEGADO.')
else:
    print('Empréstimo APROVADO!')