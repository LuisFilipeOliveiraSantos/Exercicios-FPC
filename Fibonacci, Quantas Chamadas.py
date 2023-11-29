# OBS : Dentro da arvore binaria como exemplo, se quisermos o fib de (5) iremos somar o fib(4) = 8 + fib(3) = 4 + 2 que seria o proprio caso de fib(3) e fib(4)
# Mesma coisa com o Fib(4) que iriamos somar fib(3) = 4 + fib(2) = 2 + 2 que seria o proprio caso f(3) e fib(2)
# No meu caso eu já adicionei o + 2 dentro da variavel B.



N = int(input())

def fibonacci(X):
    if X == 0:
        return 0, 0
    elif X == 1:
        return 1, 0

    fib = [0] * (X + 1)
    num_calls = [0] * (X + 1)
    fib[1] = 1
    num_calls[1] = 0

    for i in range(2, X + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        num_calls[i] = num_calls[i - 1] + num_calls[i - 2] + 2
    print(fib)
    return fib[X], num_calls[X]

for i in range(N):
    X = int(input())
    resultado, num_calls = fibonacci(X)
    print(f"fib({X}) = {num_calls} calls = {resultado}")
   



    