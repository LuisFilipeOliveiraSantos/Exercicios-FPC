n = int(input("Digite um número: "))

def F(n):
    if n < 4:
        return 3
    else:
        return F(2) * F(n - 4) + 5

resultado = F(n)
print(resultado)