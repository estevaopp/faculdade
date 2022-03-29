# 13) Faça um programa para ler 2 números inteiros, e apresente o quociente e o resto da divisão
# entre eles.

num1 = int(input("escreva um numero inteiro: "))

num2 = int(input("escreva outro numero inteiro: "))

quociente = num1//num2

resto = num1%num2

print(f"quociente = {quociente}")
print(f"resto = {resto}")