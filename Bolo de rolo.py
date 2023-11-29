n = int(input("Digite a quantidade de pessoas: "))
k = int(input("Digite a quantidade de bolos: "))
tamanho = []

for i in range(k):
    t = int(input(f"Digite o tamanho do bolo {i + 1}: "))
    tamanho.append(t)


def corte(x, tamanho, n):
    cortado = [(y // x) for y in tamanho]
    print(f"x: {x}, cortado: {cortado}")
    
    if sum(cortado) >= n:
        return x
    else:
        return corte(x - 1, tamanho, n)


resultado = corte(max(tamanho), tamanho, n)
print(resultado)
