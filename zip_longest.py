from itertools import zip_longest
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]
z2 = zip_longest(l1, l2, fillvalue=0)
print(list(z2))