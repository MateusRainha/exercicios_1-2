"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha

Exemplo da estrutura de armazenamento das vendas:

    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]

    ou então:

    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]


"""

if __name__ == '__main__':
    vendas = [
        #   ter pico fai gra sjr
        [10, 20, 30, 40, 50],  # Gasolina
        [15, 25, 35, 45, 55]  # Gasoleo
    ]
    print(vendas)

    for venda in vendas: #deu-se o nome a cada lista de "venda"
        print(venda) #"imprimiu-se" as 2 listas em "vendas" separadamente
        for v in venda: #deu-se o nome de "v" a cada elemento dentro de cada lista "venda"
            print(v) #"imprimiu-se" cada elemento de cada lista individualmente

    x = 0
    y = 0

    print(f'vendas[x][y]={vendas[x][y]}')

    for x in range(2):
        for y in range(5):
            print(f'vendas[{x}][{y}]={vendas[x][y]}')
            print('xxxx') #é repetido 10x porque o x ta no range 2 e o y no range 5 (2x5=10) -- se o x tivesse no range 3 era 15, range 4 20

    print()
    for x in range(len(vendas)):
        for y in range(len(vendas[0])):
            print(f'vendas[{x}][{y}]={vendas[x][y]}')
        print('xxxx') #é repetido 2x porque o x ta no range 2

    #total de vendas
    total_vendas = 0
    for x in range(2):
        total_linha = 0
        for y in range(5):
            print(f'vendas[{x}][{y}]={vendas[x][y]}')
            total_vendas = total_vendas + vendas[x][y]
            total_linha = total_linha + vendas[x][y]
        print(f'total_linha={total_linha}')
    print(f'total_vendas={total_vendas}')
    #a 1 vez q o total_vendas aparece é o total de vendas da gasolina e a 2 vez o total de vendas