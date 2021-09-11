nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Com media = {media}, o aluno está REPROVADO.')
elif media >= 5.0 and media < 7:
    print(f'Com media = {media}, o aluno está de RECUPERAÇÃO.')
else:
    print(f'Com media = {media}, o aluno foi APROVADO!')