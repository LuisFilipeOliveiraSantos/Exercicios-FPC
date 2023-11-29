# A penas um While

palavra = input("Digite sua palavra: ")
tamanho_da_string = len(palavra)

separacao = []

for inicio in range(tamanho_da_string):
    indice_inicial = inicio
    while indice_inicial < tamanho_da_string:
        sub_string = palavra[inicio:indice_inicial + 1]
        separacao.append(sub_string)
        indice_inicial += 1

print(separacao)




# Com 2 whiles

palavra = input("Digite sua palavra: ")
tamanho_da_string = len(palavra)

separacao = []

indice_inicial = 0
proximo_indice = 1

while indice_inicial < tamanho_da_string:
    proximo_indice = indice_inicial + 1
    while proximo_indice <= tamanho_da_string:
        sub_string = palavra[indice_inicial:proximo_indice]
        separacao.append(sub_string)  
        proximo_indice += 1   
    indice_inicial += 1
   
    
print(separacao)



