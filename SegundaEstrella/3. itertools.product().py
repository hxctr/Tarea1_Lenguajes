from itertools import product
lista1= map(int,input().split())
lista2= map(int,input().split())

print(*product(lista1,lista2))