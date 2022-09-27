#cadastrar 5 valores e posicionar na ordem mostrando as posicoes, sem usar o sort()
valor = []
for c in range(0, 5):
    v = int(input(f'{c+1}º valor: '))
    if c == 0 or v > valor[-1]:
        print("Adicionado por último")
        valor.append(v)
    else:
        for cc in range(0, len(valor)):
            if v < valor[cc]:
                valor.insert(cc, v)
                print(f'Adicionado pa posição {cc}')
                break