#Detalhado jogador, partidas, gols de cada partida 
todos = []
jogador = {}
gols = []

def leiaint(msg):
    while True:
        try:
            r = int(input(msg))
        except:
            print('Digite um valor válido')
        else:
            return r

while True:
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogador['partidas'] = leiaint('Partidas disputadas: ')
    for c in range(0, jogador['partidas']):
        gols.append(leiaint(f'Gols na partida {c+1}: '))
    jogador['gols'] = gols.copy()
    todos.append(jogador.copy())
    while True:
        cont = str(input('Continuar? s/n: ')).strip().lower()
        if cont == 'n' or cont == 's':
            break
    print('=' * 40)
    if cont in 'n':
        break
print(f'{"Cód":<7}', end='')
for k in jogador.keys():
    print(f'{k:<11}', end='')
print(' \n ')
for c, t in enumerate(todos):
    print(f'{c+1:<7}', end='')
    for v in t.values():
        print(f'{str(v):<11}', end='')
    print()
print('=' * 40)
while True:
    qual = leiaint('Desempenho de qual jogador [999 sair]? (Cód): ')
    if 0 < qual <= len(todos):
        print(f'Desempenho de {todos[qual-1]["nome"]}:')
        for c in range(0, todos[qual-1]["partidas"]):
            print(f'  Partida {c+1}: {todos[qual-1]["gols"][c]} gols.')
            print('=' * 40)
    elif qual == 999:
        break
    else:
        print('Cód inválido.')