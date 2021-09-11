from math import pow
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('A sua altura em cm: '))

imc = peso / pow(altura, 2)
print(f'O imc dessa pessoa é igual a {imc:.2f}Kg.')
if imc < 18.5:
    print('Você está ABAIXO do peso ideal.')
elif imc < 25.0:
    print('Você está no PESO NORMAL.')
elif imc < 30:
    print('Você está com SOBREPESO.')
elif imc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')