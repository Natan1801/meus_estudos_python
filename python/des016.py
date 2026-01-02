import random

alunos = input('Digite o nome do aluno: ').split()

escolhido = random.choice(alunos)

print(f'O vagabundo escolhido para apagar o quadro foi {escolhido}')
