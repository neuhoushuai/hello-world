#coding=utf-8
import time #python标准内置模块
import stand #引用自建模块 生成该模块的pyc文件
import sys #sys.getrefcount()方法可以查看 对象 python内部的引用计数
print time.time() #当前时间戳
print stand.__doc__
print stand.new_str
print stand.helloworld()
print stand.helloworld.__doc__

"""
python中一切皆对象 4 [4,5,6] "str"
变量赋值：一切变量都是对数据对象的引用
"""
d=4
d=[1,2,3]

"""
d存储的是字符串对象"haha"的位置
"""
d="haha"
e="haha"
f="haha"

#查看"haha"当前的引用计数
print sys.getrefcount("haha")

#把变量引用其他的数据对象 "haha"的引用计数减少 没有引用就销毁
d=4
e=4
f=4
print sys.getrefcount("haha")

#多重赋值
a,b,c="str","str1",4

#删除变量
del a,b,c

"""
type(a)确定数据类型
help(time.sleep)学习其它模块的功能
dir(time)看有哪些可用的方法
"""
a=1
