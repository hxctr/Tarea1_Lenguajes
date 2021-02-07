from itertools import combinations

entrada = int(input())
listaCaracteres = input().split()
entrada2 = int(input())

contador = 0;
total = 0;

for i in combinations(listaCaracteres,entrada2):
    contador += 'a' in i
    total += 1
    
print(contador/total)