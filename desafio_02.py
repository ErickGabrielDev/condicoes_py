# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    
    multa = (velocidade - 80) * 7
    print(f'Você foi multado e o valor da multa será de: R${multa}.')    
print('Parabéns você está na velociaade permitida!!')