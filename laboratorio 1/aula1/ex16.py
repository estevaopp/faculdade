"""
16) Leia 2 valores para as variáveis A e B, efetuar a troca dos valores de forma que a variável A
passe a possuir o valor da variável B, e que a variável B passe a possuir o valor da variável A.
Apresentar os valores trocados pelas variáveis.
"""

a = input("valor de A: ")
b = input("valor de B: ")

c = a
a = b
b = c

print(f"A = {a}")
print(f"B = {b}")