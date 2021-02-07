import collections

entero = int(input())
spliteado = ','.join(input().split())
Alumno = collections.namedtuple('Student',spliteado)

sum = 0
for i in range(entero):
    row = input().split()
    alumno = Alumno(*row)
    sum += int(alumno.MARKS)

print(sum/entero)