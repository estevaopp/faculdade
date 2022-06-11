# 15) Muitos países estão passando a usar o sistema métrico. Preparar um algoritmo para executar
# a conversão de Celsius para Fahrenheit.
# (0 °C × 9/5) + 32 = 32 °F

celsius = float(input("grau em celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"celsius = {celsius}")
print(f"fahrenheit = {fahrenheit}")
