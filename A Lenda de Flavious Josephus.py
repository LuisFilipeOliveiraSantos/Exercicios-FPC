NC = int(input())

def elimina(n, k):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        pessoas = list(range(1, n + 1))
        excluir = 0   
        while len(pessoas) > 1:
            excluir = (excluir + k - 1)  % len(pessoas)
            del pessoas[excluir]        
        return pessoas

for i in range(NC):
    n, k = map(int, input().split())
    resultado = elimina(n, k)
    print(f"Case {i + 1}: {resultado}")
   
    