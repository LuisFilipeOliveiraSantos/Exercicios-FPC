N = int(input("Quantas vezes os interruptores foram apertados?: "))

lampada_A = 0
lampada_B = 0

for i in range(N):
    interruptor = int(input("Digite qual interruptor foi apertado (1 ou 2): "))
    
    if interruptor == 1:
        lampada_A = 1 - lampada_A
    elif interruptor == 2:
        lampada_A = 1 - lampada_A
        lampada_B = 1 - lampada_B

print(lampada_A)
print(lampada_B)

