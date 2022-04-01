from unittest import result


num = int(input("numero para calculo de fatorial: "))

def fatorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result
        
            
print(fatorial(num))
