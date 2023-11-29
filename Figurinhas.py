N = int(input())

def MDC(x , y):
    if x % y == 0:
        return y
    elif y % x == 0:
        return x
    else:
        return MDC(y , x % y)
   
for i in range(N):
    try:
        F1, F2 = map(int, input().split())
        resultado =  MDC(F1, F2)
        print(resultado)
    except:
        print("Entrada invalida")
        
