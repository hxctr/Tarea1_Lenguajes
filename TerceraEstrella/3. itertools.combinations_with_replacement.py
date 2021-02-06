from itertools import combinations_with_replacement

lista = input().split();
listaCaracteres = sorted(lista[0]);
numero = int(lista[1]);

for i in combinations_with_replacement(listaCaracteres,numero):
    print(''.join(i));