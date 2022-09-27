# sortear x jogos de mega sena
from random import randint
todos = []
jogo = []
qnts = int(input('Quantos jogos: '))
for c in range(0, qnts):
    for j in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                break
    todos.append(jogo[:])
    jogo.clear()
print()
for c, t in enumerate(todos):
    print(f'Jogo {c+1}: {sorted(t)}')