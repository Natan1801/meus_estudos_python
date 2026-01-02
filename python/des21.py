velocidade = float(input('Digite a velocidade atual do carro: '))
if velocidade > 80 :
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa R${multa:.2f}')
    print('Tenha um bom dia, dirija com segurança!')