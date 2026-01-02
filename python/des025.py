casav = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite quantos anos você irá pagar: '))
prestação =  casav /(anos * 12)
minimo = salario * 30 / 100
print(f'Para realizar a compra de uma casa por R${casav:.2f}, em alguns anos {anos}, a prestação será {prestação:.2f}')
if prestação <= minimo:
    print('Emprestimo aceito!')
else:
    print('Emprestimo negado!')
    
