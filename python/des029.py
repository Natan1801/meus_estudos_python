nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media}')
if media < 5.0:
    print(f'Aluno está reprovado, com a média {media:.1f}')
elif media >=5 and media < 7:
    print(f'Aluno está em recuperação, com a média {media:2f}')
elif media >= 7.0:
    print(f'Aluno Aprovado, com a média {media:.1f}')         