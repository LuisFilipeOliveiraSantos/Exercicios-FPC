
Viagens = 3
caixas = []

for i in range (3):
    caixa = int(input(f"Digite o tamanho da caixa {chr(65 + i)}: "))
    caixas.append(caixa)


caixas.sort()

if caixas[0] + caixas[1] <= caixas[2]:
   print(Viagens = 1)

elif caixas[0] == caixas [1] == caixas[2]:
    print(Viagens = 3)

else:
    print(Viagens = 2)



