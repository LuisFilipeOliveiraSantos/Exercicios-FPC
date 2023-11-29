
sequencia = int(input("Quantos números tem a sequência? "))

pilares = []

if sequencia < 3 or sequencia >= 10000:
    print("A sequencia de números deve ser maior que 3 e menor ou igual a 10000!")    
else:
    for i in range (sequencia):
        altura = int(input(f"Digite a altura do pilar número {1 + i}: "))
        if altura < 1:
            print("A altura dos pilares deve ser maior ou igual a 1!")
            break      
        else:
            pilares.append(altura)


def escher (pilares):
    quantidade = len(pilares)

    for i in range (quantidade - 1):
        if not (pilares[i] + pilares[quantidade - i - 1] == pilares[i + 1] + pilares[quantidade - 2 - i]):
           return "N"
        
    return "S"

resultado = escher(pilares)

print(resultado)


     

