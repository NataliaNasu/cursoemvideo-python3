'''texto'''

frase = 'Curso em vídeo Python'
print(frase[9])
print(frase[:10])
print(frase[15:])
print(frase[9:13])
print(frase[9:21])
'''ele vai até o 20, mas não é mto recomendado'''
print(frase[9:21:2])
'''inicio, fim, salto -> v, d, o, P, t, o'''
print(frase[9::3])

'''tamanho do texto'''
print(len(frase))
'''contar as repetições'''
print(frase.count('o'))
'''contagem, com fatiamento, lista, inicio, fim'''
print(frase.count('o', 0, 13))
'''encontra o texto e a posição de onde começou o texto > 11'''
print(frase.find('deo'))
'''pd juntar funções: se quiser procurar pela letra 'o', 
nesta frase só terá em maiúscula, então, transforma a frase
em maíscula e achará a letra'''
print(frase.upper().count('O'))
'''Se, não for encontrado, irá mostrar -1'''
print(frase.find('Android'))

'''Uso do moderador IN, mas só retorna true ou false'''
print('Curso' in frase)

'''transformação = trocar, mas transforma de forma secundária,
ou seja, não se altera o objeto original'''
print(frase.replace('Python', 'Android'))
'''pra salvar os dados precisa fazer a atribuição:
frase = print(frase.replace('Python', 'Android'))'''

'''todas MAIÚSCULAS'''
print(frase.upper())
'''tudas minúsculas'''
print(frase.lower())
'''coloca td em minúscula e coloca a 1a letra em maiúscula'''
print(frase.capitalize())
'''determina a quantidade de palavras pelos espaços, 
e capitalize palavra por palavra'''
print(frase.title())

'''Remove todos os espaços vazios do início e do fim'''
frase2 = '   Aprenda Python  '
print(frase2.strip())
'''Remove somente os espaços do lado direito'''
print(frase2.rstrip())
'''Remove somente os espaços do lado esquerdo'''
print(frase2.lstrip())

'''Divisão'''
'''observa os espaços, e ocorre uma divisao na string e,
cada palavra se torna um índice de uma nova lista.'''
print(frase.split())
'''Junção'''
print('-'.join(frase))

'''Se o split cria outra lista'''
dividido = frase.split()
'''o print abaixo vai mostra, o conteúdo do índice 0 = Curso'''
print(dividido[0])
'''ou, dá pra encontrar um caracter em específico [3],
na string [2] = 'e'.'''
print(dividido[2][3])