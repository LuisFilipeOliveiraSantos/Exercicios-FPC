posicao_R = int(input("Digite a distancia do robô para o inicio da quadra: "))

if posicao_R < 0 or posicao_R > 2000:
    print("Posição do Robô deve ser maior ou igual a 0 e menor ou igual a 2000")
else:
    if posicao_R <= 800:
        print("1")
    elif 800 < posicao_R <= 1400:
        print("2")
    elif 1400 < posicao_R <= 2000:
        print("3")