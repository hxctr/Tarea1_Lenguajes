from itertools import *

entrada = input()
for i,j in groupby(map(int,list(entrada))):
    print(tuple([len(list(j)), i]) ,end = " ")