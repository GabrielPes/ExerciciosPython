#nome, idade, sexo, cont?
#tot cadastradas, media de idade, quais sao mulheres, lista pessoas acima da media idade
todos = []
pessoa = {}
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        try:
            id = int(input('Idade: '))
        except:
            print('Digite uma idade')
        else:
            pessoa['idade'] = id
            break
    while True:
        s = str(input('Sexo M/F: ')).strip().lower()
        if s == 'f' or s == 'm':
            pessoa['sexo'] = s
            break
        else:
            print('Digite M ou F.')
    todos.append(pessoa.copy())
    while True:
        cont = str(input('Continuar? S/N: ')).strip().lower()
        if cont == 's' or cont == 'n':
            break
    if cont in 'n':
        break
print('=' * 40)
print(f'{len(todos)} pessoas cadastradas')
tot = 0
print(f'Mulheres', end='')
for t in todos:
    if t['sexo'] == 'f':
        print(f' - {t["nome"]}', end='')
    if t['idade']:
        tot += t['idade']
media = tot / len(todos)
print()
print(f'Média de idade: {media:.1f} anos')
print('Acima da média de idade', end='')
for t in todos:
    if t['idade'] >= media:
        print(f' - {t["nome"]}', end='')
print()