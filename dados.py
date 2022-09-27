#perguntar: nome, ano, carteira trab(0 n tem), ano contratacao, salario
#mostrar: nome, idade, ctps, contratacao, sal, aposentadoria(35anos cont)
pessoa = {}
from datetime import datetime
atual = datetime.now().year
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
while True:
    try:
        nasc = int(input('Ano de nascimento: '))
    except:
        print('Valor inválido.')
    else:
        if 1900 < nasc < atual:
            break
        else:
            print('Data incorreta')
            continue
pessoa['idade'] = atual - nasc
pessoa['ctps'] = int(input('CTPS [0]Não tem: '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - nasc
print('=' * 30)
for k, v in pessoa.items():
    print(f'{k.upper()}: {v}')