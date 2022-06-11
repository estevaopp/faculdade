"""
12) Escreva um algoritmo para determinar o consumo médio de um automóvel sendo que será
fornecida via teclado a distância total percorrida pelo automóvel e o total de combustível gasto.
"""

distance = float(input("Escreva a distancia percorrida em quilometro: "))

combustivel = float(input("Escreva o combustivel gasto em litro: "))

consumo_medio = distance/combustivel

print(f"consumo médio igual {consumo_medio:.2f}kg/L")
