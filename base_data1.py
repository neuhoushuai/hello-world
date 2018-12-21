#coding=utf-8
"python 基本数据练习"

"""
数据组成：身份ID、类型、值
类型：int string boolean list tuple dict
    不可变类型：int、string、tuple
    可变类型：list、dict
"""
a=1
if __name__=="__main__":
    if id(a)==id(1):
        print True  #布尔值
        print id(a) #数据的标识符
        print type(a) #数据类型
    a="haha"
    if id(a)!=id(1):
        print False
        print id(a)
        print id(1)

    """
    可变类型展示
    """
    e=[1,2,3]
    print id(e)
    e.append(4)
    print e
    print id(e)

    """
    类型转换展示
    """
    a="12345"
    print int(a)+1
    a=bool(id(a)==id("12345"))
    print a

    "homework"
    info="abc"
    newstr=info.replace("c","e") #replace方法修改
    newstr=list(info) #list转换 join新建字符串方法
    newstr[2]="e"
    newstr=info[0:2]+'e'#序列切片重组
    print (newstr)
    
