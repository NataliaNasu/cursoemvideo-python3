from math import hypot

catAdj = int(input('Informe o cateto adjacente: '))
catOp = int(input('O cateto oposto: '))
hipotenusa = hypot(catOp, catAdj)
print(f'O cateto da hipotenusa é igual a {hipotenusa:.2f}.')