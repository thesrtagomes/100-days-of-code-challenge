soma_notas = 0
matérias = 0


nota = float(input('Qual a minha nota? '))
while True:
    try:
        soma_notas += nota
        matérias += 1
        nota = float(input('Qual a minha nota? '))
    except ValueError:
        break
média = soma_notas / matérias
print(f'{média:.2f}')
