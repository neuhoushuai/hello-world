#coding:"utf-8"
import math
a=[1,2,3,4,5,6,7]
"""
有序、索引、嵌套、可变类型 
"""
a[0:4:1] 
a[-1:-4:-1] #反向索引
a[1:]#默认索引
a[1::2]#步长2索引

"""
添加列表
"""
b=[4,5,6]
c=a+b #新建列表
print id(a)
a.append(4) #原地末尾添加数据元素
print id(a)
a.insert(1,[1,2])
print a
a.extend(b) #将b中的每个元素都添加到列表中
print a


"""
修改元素
"""
A=[1,2,3]
A[0]="哈哈" #这个是gbk编码存的？？？？
print A

"""
删除列表元素
"""

a=[2,3,4,5]
del a[0]
a.remove(3) #删除第一个匹配，没有的话抛出异常
print a
print a.pop() #删除最后一个

"""
判断元素是否在列表里
"""
a=[1,2,3,4,5]
print 3 in a
print 4 not in a

"""
列表推导式
[exp for iter_var in iterable if cond_exp]
iterable：迭代器生成的内容每次迭代放到iter_var中
exp用iter_var中的内容
"""
print [math.pow(x,2) for x in range(1,11) if x%2==0]

"""
排序？？
"""
a=[222,44,66,33,66]
b=a.sort()
print b
if b == None: #b is None
    print 'haha'

"""
homework
"""
a=[1,2,3,4,5,333,11,44]
print a[3:6]
a=[1,2,3]
b=[4,5,6]
print a+b
a.extend(b)
print a
a=[1,99,33,44,55,22]
a.append((11,33,54))
a=[1,99,33,44,55,22]
a.insert(3,101)
a.insert(1,2)
a=[x for x in range(21,101) if x%2==0]
