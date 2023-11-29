# FORMA RECURSIVA

n = int(input("Digite a quantidade de pessoas: "))
k = int(input("Digite a quantidade de pessoas que vão ser escolhidas: "))


def combinacao(n,k):
    if  n <= 1:
        return "o valor deve ser maior ou igual a 1"
    else:
        if k == n:
            return 1 
        if k == 1:
            return n
        else:
            return combinacao(n - 1 , k - 1 ) + combinacao(n - 1, k)


resultado = combinacao(n,k)

print(f"comb({n}, {k} = {resultado})")



# FORMA NÃO RECURSIVA

def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1 , n + 1):
        resultado *= i
    return resultado


def combinacao(n, k):
    if n >= k >= 0:
        return fatorial(n) // (fatorial(k) * fatorial(n - k))
    else:
        return 0



calculo = combinacao(n, k)
print(calculo)
    