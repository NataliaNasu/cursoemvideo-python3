#leia o sexo, até a entrada ser F/M.

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
        sexo = str(input('Dados inválidos! Informe seu sexo: [M/F] ')).strip().upper()
print(f'O sexo: {sexo}, foi registrado com sucesso!')
