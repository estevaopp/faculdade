num = int(input("Escreva o numero de fibonacci desejado: "))

def fibonacci(num):
    fibonacci_sequence = []
    for n in range(num+1):
        if n == 0 or n == 1:
            fibonacci_sequence.append(n)
        else:
            next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_num)
    return fibonacci_sequence[-1]


def fibonacci_sequence(num):
    fibonacci_sequence = []
    for n in range(num+1):
        if n == 0 or n == 1:
            fibonacci_sequence.append(n)
        else:
            next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_num)
    return fibonacci_sequence


fibonacci_num = fibonacci(num)

sequence = fibonacci_sequence(num)

print(sequence)

print(fibonacci_num)