"""17) Faça um programa para calcular e apresentar o volume de uma lata de óleo, utilizando a
fórmula volume = 3.14159 ∗ raio ∗ raio ∗ altura. Identifique na fórmula os valores de entrada de
dados e leia-os via teclado."""

raio = float(input("informe o raio: "))

altura = float(input("informe o altura: "))

volume = 3.14159 * raio * raio * altura

print(f"volume = {volume}")