# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, Calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 

salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100) 
    print(f'Seu novo salário é: R${aumento:.2f}')
else:
    aumento = salario + (salario * 10 / 100)  
    print(f'Seu novo salário é: R${aumento:.2f}')
