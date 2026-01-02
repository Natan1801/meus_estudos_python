from random import randint
pc = randint(0, 5)
print(f'Vou pensar em um número entre 0 e 5...')
jogador = int(input('Digite um número: '))

if jogador == pc:
    print('Parabéns! Você acertou')
else:
    print(f'Pensei no número {pc} e não no número {jogador}')