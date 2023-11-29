
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

    return fib[X], num_calls[X]

for i in range(N):
    X = int(input())
    resultado, num_calls = fibonacci(X)
    print(f"fib({X}) = {num_calls} calls = {resultado}")
