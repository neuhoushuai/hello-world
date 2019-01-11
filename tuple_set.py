#coding:utf-8
"""
修改元组
"""
a=(1,2,3)
b=list(a)
b[0]=4
a=tuple(b) #新建了一个元组

"""
元组保证数据安全示例
"""
a=[1,2,3]
def info(a):
    #b=a[:] b[0]="haha" 新建变量拷贝防止数据改变 传元组防止数据改变
    print "a\'s id: %d" % id(a)
    a[0]="haha"
    return a
print a
info(a)
print a

"""
集合：无序不能切片索引（只有键值的字典）
a=set(iterable) 参数传入可迭代对象创建可变集合对象
    可迭代对象简单判断方法：dir(int)/dir(list) 方法中有__iter__  是可迭代对象
"""
a=set('abc')#可变集合对象
a.add('python')#整体添加元素
a.update('python')#将每个元素加入集合
a.remove('python')#删除元素
if 'c' in a: #成员关系 in / not in
    print True
a=set('abcd')
b=set('bcdef')
print a&b #集合交集
print a|b #集合并集
print a-b #集合差集
"""
利用集合去重复
"""
a=[1,2,3]
a.append(3)
a.append(1)
a=set(a)
a=list(a)

"""
不可变集合
"""
a=frozenset('abc')

"""
homework
"""
a=(1,2,3)
b=list(a)
b[0]=5
a=tuple(b)

a=set('abc')
a.add('jay')
b=set('befg')
c=a|b
c=a.update(b)

