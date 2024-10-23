def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Informe um numero: "))

n = 0


while fibonacci(n) <= num:
    if fibonacci(n) == num:
        print("O numero pertence a sequência de Fibonacci.")
        break
    n += 1
else:
    print("O numero nao pertence a sequência de Fibonacci.")
