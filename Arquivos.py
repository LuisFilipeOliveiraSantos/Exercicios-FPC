n = int(input("Digite a quantidade de arquivos: "))
b = int(input("Digite o limite de bytes da pasta: "))
tamanho = []

for i in range(n):
    N = int(input(f"Digite o tamango do arquivo {i + 1}: "))
    
    if N > b:
        print("O tamanho dos arquivos devem ser menor ou igual ao limite da pasta")
        exit()
    else:
        tamanho.append(N)
        

def somar(lista):
    if len(lista) == 1:
        return lista[0]
    elif len(lista) > 1:
        return lista[0] + somar(lista[1:])
    else:
        print("Lista está vazia")
        exit()

resultado = somar(tamanho)
print(f"A quantidade de pastas necessárias será: {resultado // b}")