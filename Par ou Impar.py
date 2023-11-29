P = int(input("Digite 0 para Alice ser par ou digite 1 para Bob ser par: "))

D1 = int(input("Digite a quantidade de dedos que Alice colocou: "))
D2 = int(input("Digite a quantidade de dedos que Bob colocou "))

def ganhador (P,D1,D2):
    if (D1 + D2) % 2 == 0 and P == 0:
        return 0
    elif (D1 + D2) % 2 != 0 and P == 0:
        return 1
    elif (D1 + D2) % 2 == 0 and P == 1:
        return 1
    else:
        return 0
    
quem_ganhou = ganhador(P,D1,D2)

print(quem_ganhou)