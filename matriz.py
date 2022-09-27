#matriz 3x3 // Soma de todos os pares // Soma da terceira coluna // Maior vlor da seg linha
matriz = [[], [], []]
soma3col = maior2linha = 0
for lin in range(0, 3):
    for col in range(0, 3):
        while True:
            try:
                n = int(input(f'Valor col{lin} / lin{col}: '))
            except:
                print('Digite um número.')
            else:
                matriz[lin].append(n)
                break
        if col == 2:
            soma3col += n
        if lin == 1:
            if col == 0:
                maior2linha = n
            else:
                if n > maior2linha:
                    maior2linha = n
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'{matriz[lin][col]:<5}', end='')
    print()
print(f'Soma da 3ª coluna: {soma3col}')
print(f'Maior da 2ª linha: {maior2linha}')