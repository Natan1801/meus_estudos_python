distancia = float(input('Digite a distância da sua viagem: '))
print(f'Você está prestes a começar uma viagem de {distancia}Km')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
    print(f'O preço da sua passagem é R${preço:.2f}')