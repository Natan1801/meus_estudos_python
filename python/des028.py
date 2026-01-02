from datetime import date
atual = date.today().year
nasci = int(input('Digite a data de nascimento: '))
idade = atual - nasci
if idade == 18: 
    print(f'Terá que servir pois, ele tem {idade}')
elif idade < 18:
    saldo = 18 - idade
    print(f'Não está na hora, pois ele ainda possui {idade}')    