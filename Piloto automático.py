carro_A = int(input("Digite a posição do carro A: "))
carro_B = int(input("Digite a posição do carro B: "))
carro_C = int(input("Digite a posição do carro C: "))

# Distancia carro B para carro A
Distancia_B_A = carro_B - carro_A

# Distancia Carro C para Carro B
Distancia_C_B = carro_C - carro_B

# Acelera
if Distancia_B_A < Distancia_C_B:
    print(1)

# Mantem velocidade
elif Distancia_B_A ==  Distancia_C_B:
    print(0)

# Desacelera
elif Distancia_B_A > Distancia_C_B:
    print(-1)