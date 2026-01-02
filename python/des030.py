from datetime  import date

atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = nascimento - atual

if idade <= 9:
    print(f'O altleta tem {idade}.')
    print('Categoria: MIRIN')
elif idade <= 14:
    print(f'O atleta tem {idade}.')
    print('Categoria: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade}')
    print('Categoria: JUNIOR')
elif idade <= 20:
    print(f'O atleta tem {idade}')
    print('Categoria: SÊNIOR')
else:
    print(f'O atleta tem {idade}')
    print('Categoria: MASTER')          