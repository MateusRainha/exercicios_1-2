if __name__ == '__main__':
    vendas = [
        #   ter pico fai gra sjr
        [10, 20, 30, 40, 50],  # Gasolina
        [15, 25, 35, 45, 55]  # Gasoleo
    ]
    print(vendas)
    print()

    for venda in vendas:
        print(venda)
        for v in venda:
            print(v)
            print()

    x = 0
    y = 0

    for y in range(5):
        soma_ilhas = 0
        for x in range(2):
            print(f'x={x} y={y}')
            print(f'[{x}][{y}]')