# def chamadas(n, b):
#     if n <= 0 or n >= 2**63 - 1 or b <= 0 or b > 10000:
#         return 0 
#     else:
#         contagem = [0] * (n + 1)
#         contagem[1] = 0
#         for i in range(2, n + 1):
#             contagem[i] = contagem[i - 1] + contagem[i - 2] + 2
#         return contagem[n]

# numero_caso = 1

# try:
#     NC = int(input())
#     numero_caso = 1

#     test_cases = []

#     for i in range(NC):
#         n, b = map(int, input().split())
#         test_cases.append((n, b))

#     for n, b in test_cases:
#         resultado = chamadas(n, b)
#         base = (resultado + 1) % b
#         print(f"Case {numero_caso}: {n} {b} {base}")
#         numero_caso += 1
# except ValueError:
#     print()




def chamadas(n, b):
    if n <= 1:
        return 0
    else:
        a, y = 2, 4
        contagem = 0
        for i in range(3, n):
            contagem = a + y + 2
            a, y = y, contagem
        return y % b

numero_caso = 1
while True:
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break
    resultado = chamadas(n, b)
    print(f"Case {numero_caso}: {n} {b} {resultado + 1}")
    numero_caso += 1