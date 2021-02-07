from itertools import product

K,M = map(int,input().split())
numeros = []
for _ in range(K):
    columna = map(int,input().split()[1:])
    numeros.append(map(lambda x:x**2%M, columna))
print(max(map(lambda x: sum(x)%M, product(*numeros))))