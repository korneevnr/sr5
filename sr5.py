def two (n):
    s=''
    while n>0:
        ost=n%2
        s=s+str(ost)
        n=n//2
    s = s[::-1]
    return s

def eight (n):
    s=''
    while n>0:
        ost=n%8
        s=s+str(ost)
        n=n//8
    s = s[::-1]
    return s


n = int(input("Введите число: "))
sys = int(input("Введите целевую систему счисления: "))
#print(bin(n)[2:])
#print (oct(n)[2:])
if sys == 2: print(two(n))
if sys == 8: print(eight(n))


