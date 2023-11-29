def print_possiveis_sucessoes_gols(m, n, sequencia_atual=""):
    if m == 0 and n == 0:
        print(sequencia_atual)
    if m > 0:
        print_possiveis_sucessoes_gols(m - 1, n, sequencia_atual + "A ")
    if n > 0:
        print_possiveis_sucessoes_gols(m, n - 1, sequencia_atual + "B ")

# Exemplo de uso:
m = 3
n = 1
print_possiveis_sucessoes_gols(m, n)