#usuário deve digitar uma expressão matemática que use parênteses.
#o programa deve analisar se a expressão está com parênteses
# abertos ou fechados na ordem correta.

expressao = (str(input('Informe uma expressão matemática: ')))

simbolos = []
for s in expressao:
    if s == '(':
        simbolos.append('(')
    elif s == ')':
        if len(simbolos) > 0:
            simbolos.pop()
        else:
            simbolos.append(')')
            break
if len(simbolos) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
