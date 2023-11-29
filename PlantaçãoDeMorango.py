# Terreno 1
comprimento_area1 = 12
largura_area1 =  38

# Terreno 2
comprimento_area2 = 5
largura_area2 = 20

# Área do terreno 1 e 2
area1 = comprimento_area1 * largura_area1
area2 = comprimento_area2 * largura_area2

def maior_area(area1,area2):
    if area1 > area2:
        return area1
    return area2



melhor_terreno = maior_area(area1, area2)

print(melhor_terreno)

