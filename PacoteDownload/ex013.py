salario = float(input('Digite o salário do funcionário: R$'))
novoSalario = salario + (salario * 15 / 100)
aumento = novoSalario - salario
print(f'O aumento salarial de 15% sobre R${salario},')
print(f'corresponde a R${novoSalario}, um aumento de R${aumento}')