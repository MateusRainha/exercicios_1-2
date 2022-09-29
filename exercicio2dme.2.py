ilhas = ['Terceira', 'Pico', 'Faial', 'Graciosa', 'São Jorge']
tipos = ['Gasolina', 'Gasóleo']
vendas =[
            [0,0,0,0,0],
            [0,0,0,0,0]
]

if __name__ == '__main__':
    # Obter input
    for x in range(2):
        for y in range(5):
            while True:
                try:
                    vendas[x][y] = int(input(f'Insira vendas de {tipos[x]} para a ilha {ilhas[y]} '))
                    break
                except ValueError:
                    print(f'Insira um valor válido para vendas de {tipos[x]} na ilha {ilhas[y]}')
    print(vendas)

    # Imprimir vendas por tipo



    # Imprimir vendas por ilha