num = int(input('Digite um número para a conversão: '))
op = int(input('Escolha a conversão: 1 - Binário, 2 - Octal, 3 - Hexadecimal: '))

if op == 1:
    print(f'Binário: {format(num,'b')}')
elif op == 2:
    print(f'Octal: {format(num, 'o')}')
elif op == 3:
    print(f'Hexadecimal: {format(num, 'x')}')
else:
    print('Opção inválida.')