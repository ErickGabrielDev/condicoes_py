# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = numero1
menor = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

