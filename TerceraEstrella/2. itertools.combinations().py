# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools


spliteado = input().split()
cadena, numero = sorted(spliteado[0]), int(spliteado[1])
for i in range(1, numero + 1):
    print(*list(map(''.join, itertools.combinations(cadena, i))), sep='\n')
