def somador(a, b):
    resultado = 0
    somar = 1
    for i in range(32):
        bit_a = (a & somar) >> i
        bit_b = (b & somar) >> i
        resultado |= (bit_a ^ bit_b) << i
        somar <<= 1

    return resultado


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    resultado = somador(a, b)
    print(resultado)
