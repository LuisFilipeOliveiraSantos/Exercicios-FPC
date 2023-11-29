x = int(input("Digite o número que vai ser elevado: "))
n = int(input("Digite o número que vai ser multiplicado: "))

def f(x, n):
    if n == 0:
        return 1
    else:       
        return x * f(x, n - 1)
        
result = f(x, n)
print(result)
        
 