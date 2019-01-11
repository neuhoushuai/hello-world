#coding:utf-8

"""
list(iterable)
参数：可迭代对象
返回：列表
"""
a=list("China")

"""
xrange 返回xrange对象（生成器）（省内存不一次性生成数据）（循环中如果不用到全部迭代）

"""
for m in xrange(1000):
    if m==10:
        print 'sss'
        break

"""
列表推导式
[exp for iter_var in iterable if cond_exp]
"""
a=[x*x for x in range(1,101)] #取出1-100以内数的平方
a=["the %s" % d for d in xrange(10)] #生成字符串列表
a=[(x,y) for x in range(2) for y in range(2)] #生成元组列表
a=dict([(x,y) for x in range(3) for y in range(2)])#生成字典(覆盖了键的值)

"""
列表引用删除注意
"""
a=[1,2,3]
b=a
del a
a=b
del a[:]
print b

"""
homework
"""
a=(1,2,3)
b=list(a)
b[2]=4
c=tuple(b)
a=["%d love python" % x for x in range(1,11)]
a=[(x,y) for x in [0,2] for y in [0,2]]
