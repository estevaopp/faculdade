# Construir um algoritmo para ler 3 valores reais, calcular e imprimir a média desses valores.

from statistics import mean

while True:
    try:
        num1 = input('numero 1: ')
        num1 = float(num1.replace(',', '.'))
        num2 = input('numero 2: ')
        num2 = float(num2.replace(',', '.'))
        num3 = input('numero 3: ')
        num3 = float(num3.replace(',', '.'))
        if type(num1) == float and type(num1) == float and type(num1) == float:
            break
    except:
        print('Escreva um numero!')

amostra = [num1, num2, num3]

media = mean(amostra)

print(media)