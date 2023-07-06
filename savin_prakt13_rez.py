import random

matr_a=[]
matr_b=[]
matr_c=[]

def print_matr(tmp):
    for i in tmp:
        print(*i)
        
print("Введите размерность матриц А и B через пробел")
print("Прим.Складывать можно только одноразмерные матрицы")
ax,ay=map(int,input().split())
print()

matr_a=[[0 for i in range(ay)] for j in range(ax)]     # инициализация
matr_b=[[0 for i in range(ay)] for j in range(ax)]     
matr_c=[[0 for i in range(ay)] for j in range(ax)]

print("Введите диапазон случайных чисел. Целые, через пробел")
n,m=map(int,input().split())
print()

for i in range(ax):
    for j in range(ay):
        matr_a[i][j]=random.randint(n,m)
        matr_b[i][j]=random.randint(n,m)
     
print("Ваша сгенерированная матрица А\n")
print_matr(matr_a)
print()
print("Ваша сгенерированная матрица В\n")
print_matr(matr_b)
print()

for i in range(ax):
    for j in range(ay):
        matr_c[i][j]=matr_a[i][j]+matr_b[i][j]
        
print("Результат сложения матриц А и В\n")
print_matr(matr_c)
