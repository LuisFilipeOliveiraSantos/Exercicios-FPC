Alunos = int(input("Quantos Alunos vão pegar o bondinho? "))
Monitores = int(input("Quantos Monitores vão pegar o bondinho? "))

Max_Bondinho = 50

def pode_ou_nao():
    if Alunos + Monitores > Max_Bondinho:
        return "N"
    return "S"

viagem = pode_ou_nao()


if  1 < Alunos and Monitores > 50:
    print("O número de alunos e monitores deve ser maior que 0 e menor ou igual  a 50!")
else:
    print(viagem)

        

    
   


