from collections import Counter, OrderedDict, deque
texto = 'Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. '
contagem = Counter(texto.split())
print(contagem.most_common(3))