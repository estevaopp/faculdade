"""19) Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar ao final do programa o seu nome, o salário fixo e salário
no final do mês."""

vendedor = input("nome do vendedor: ")

salario_fixo = float(input(f"salario fixo de {vendedor}: "))

vendas = float(input(f"total de vendas de {vendedor}: "))

comissao = 0.15

salario = vendas * comissao + salario_fixo

print(f"{vendedor} receberá R${salario}")