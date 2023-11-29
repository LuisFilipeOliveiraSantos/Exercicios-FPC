T = int(input("Digite o número de casos: "))

def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + f(n // 2)
    else:
        return 1 + f(3 * n + 1)

def G(A, B):
    maximo = 0
    for n in range(A, B + 1):
        chamadas = f(n)
        maximo = max(maximo, chamadas)
    return maximo


for caso in range(1, T + 1):
    A, B = map(int, input().split())
    resultado = G(A, B)
    print(f"Caso {caso}: {resultado}")