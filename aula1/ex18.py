"""18) Você irá fazer uma viagem internacional e precisa levar seu dinheiro em dólares. Elabore um
algoritmo para calcular e apresentar o valor da conversão de real (R$) para dólar (US$). O
algoritmo deverá solicitar o valor da cotação do dólar e quantos Reais(R$) você tem para
converter em dólar. Ao final mostre a quantidade de dólares que você irá levar para a viagem."""

cotacao = float(input("informe a cotação do dolar: "))

real = float(input("informe o dinheiro que você vai levar em reais: "))

dolar = cotacao * real

print(f"A quantidade de dólares que você irá levar para a viagem será ${dolar}")
