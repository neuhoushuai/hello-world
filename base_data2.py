#coding:utf-8
"""
"abc":字符串
"ab"：子串
unicode码
"""
a="哈哈"
b="1234"

"""
len显示的是字节长度
"""
print len(a)
print len(b)


c=u"哈哈" #转Unicode 正确计算字符长度值
print len(c)
g=a.decode('utf-8')

"""
转义符号
"""
a='abc\''
a='abc\n'
a=r'abc\n' #不要转义

"""
格式化字符串
"""
a="This is a %s" % "apple" # %占位符 
a="This is a %s" % 4 #强行类型转换
a="This is a %s and %s" % ("banana",5)
b="This is a {1} and {0}".format("lemon","orange") #{}里边是占位的位置
b="This is a {people}{fruit}".format(fruit="orange",people="my")
