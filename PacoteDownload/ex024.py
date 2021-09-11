cidade = str(input('Digite o nome de uma cidade: ')).strip()
#primeiroNome = cidade.split()
#comeca = primeiroNome[0] == 'SANTO'
#nao = primeiroNome[0] != 'SANTO'
primeiroNome = cidade[:5].upper() == 'SANTO'
print(f'O nome dessa cidade começa com Santo? {primeiroNome}')