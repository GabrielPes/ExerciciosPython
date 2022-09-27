musicas = [
    {'titulo': 'in the end', 'tocou': 10},
    {'titulo': 'numb', 'tocou': 20},
    {'titulo': 'faint', 'tocou': 5},
]
print(min(musicas, key=lambda var: var['tocou'])['titulo'])
print(sorted(musicas, key=lambda n: n['tocou'], reverse=True))
