num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print(f'O primeiro valor {num1} é maior que o segundo valor {num2}')
elif num2 > num1:
    print(f'O segundo valor {num2} é maior que o primeiro valor {num1}')   
elif(num1 == num2 ):
   print('Não existe valor menor ou maior, todos são iguais')     