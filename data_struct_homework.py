#coding:gbk
#1
a=[11,22,24,29,30,32]
a.append(28)
a.insert(4,57)
a[0]=6
a.remove(32)
a.sort()

#2
b=[1,2,3,4,5]
#b.extend([6,7,8])
print b[-1:-3:-1]
c=b[3:5]
c.sort(reverse=True)
if 2 in b:
    print True

#3
b=[23,45,22,44,25,66,78]
