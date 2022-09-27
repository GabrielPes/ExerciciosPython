#fatorial usando função, mostrar ou nao a conta(show=true e false)

def fatorial(num, show=False):
    f = 1
    for c in range(1, num+1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c == num:
                print(' = ', end='')
            else:
                print(' x ', end='')
    print(f'Fatorial de {num} é: {f}')


fatorial(int(input('Fatorial de qual valor: ')), show=True)