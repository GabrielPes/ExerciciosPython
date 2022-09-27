#4 jogadores dados // mostrar resultado e ordem dos gaanhadores
jog = {}
from random import randint
from operator import itemgetter
for c in range(0, 4):
    nome = str(input('Nome: ')).strip().capitalize()
    jog[f'{nome}'] = randint(1, 6)
print('Jogadas:\n ')
for k, v in jog.items():
    print(f'{k}:  {v:>15}')
rank = sorted(jog.items(), key=itemgetter(1), reverse=True)
print(' \nRanking:\n ')
for c, r in enumerate(rank):
    print(f'  {c+1}º: {r[0]}')