

n = int(input("Введите кол-во элементов: "))
a = [0] * n
for i in range(len(a)):
    i = str(i + 1)
    print("Введите элемент массива " + i + ": ", end = " ")
    i = int(i)
    i = i - 1
    a[i] = int(input())
print("")


delta = int(input("Введите значение DELTA: "))
result = a.count(min(a) + delta)
print(result)