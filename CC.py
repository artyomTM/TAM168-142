system=int(input("Введите СС: "))
s=input("Введите число: ")
p=len(s)
p-=1
res=0
for i in s:
    buf=int(i)
    if buf > system:
        raise ValueError
    res+=buf * system**p
    p-=1
print(res)
