salario = float(input('Informe o seu salário: R$'))
if salario > 1250.0:
    aumento = salario * 10 / 100
else:
    aumento = salario * 15 / 100

print(f'Você receberá um aumento salarial de R${aumento:.2f}.')
print(f'E, passará a receber um total de R${salario+aumento:.2f} reais.')