# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = int(input('Digite a distância da sua viagem em km/h: '))

if distancia <= 200:
    preço = distancia * 0.50 
else:
    preço = distancia * 0.45
print(f'O preço da sua viagem será de: {preço:.2f}.')
        
    
    
