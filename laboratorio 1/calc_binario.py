num = int(input("num: "))

def calc_binario(num):
    restos = []
    while num != 0:
        restos.append(str(num%2))
        num = num//2
    restos.reverse()
    binario = "".join(restos)
    binario = int(binario)
    return binario

binario = calc_binario(num)

print(binario)


