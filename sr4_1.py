n = int(input("Размерность массива: "))
a = [0] * n

for i in range(n):
    print("a[", i, "]=", sep = "", end = "")
    a[i] = float(input())
print("Входной массив: ", a)

start = a.index(max(a)) + 1
a[start:] = [0] * (len(a) - start)
print("Результат: ", a)