# 2 Полугодие
***
## 8

count=0
from itertools import product
for a, b, c, d, e in product(range(1,8), range(8), range(8), range(8),range(8)): 
    s=str(a)+str(b)+str(c)+str(d)+str(e)
    if s.count('6')==1 and s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0: count+=1
    if s.count('6')==1 and s.index('6')==0 and int(s[1])%2==0: count+=1
    if s.count('6')==1 and s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
        count+=1
print(count)
---
from itertools import product
nums=product('01234567',repeat=5)
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
for n in nums:
    numb=''.join(n)
    sp=[]
    if numb.count('6')==1 and numb[0]!='0':
        for x in nn:
            if x in numb:
                sp.append(x)
        if not sp: 
            k+=1
print(k)
