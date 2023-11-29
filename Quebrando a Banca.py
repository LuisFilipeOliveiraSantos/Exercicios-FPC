def maior_saldo_possivel(a, b, saldo):
    saldo = list(saldo)

    saldo.sort(reverse=True)

    saldo_removido = saldo[:-b]

    print(''.join(saldo_removido))

while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break     
        saldo = input()
        maior_saldo_possivel(a, b, saldo)
    except:
        break