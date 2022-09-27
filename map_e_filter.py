teste = [
    ['gabriel', 26, 'm'],
    ['Dani', 30, 'm'],
    ['fabi', 35, 'f'],
]
filtragem = list(filter(lambda n: n[2] == 'f', teste))
mapeamento = list(map(lambda n: [n[0], n[1], 'f'], teste))