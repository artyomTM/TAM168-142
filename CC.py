while True:
    system=int(input("Введите СС(0 - выход): "))
    if system == 0:
        break
    s=input("Введите число: ")
    p=len(s)
    p-=1
    res=0
    for i in s:
        buf=int(i)
        if buf >= system:
            raise ValueError
        res+=buf * system**p
        p-=1
    print("\tРезультат: ", res)
