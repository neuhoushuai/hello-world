#coding:utf-8
"""
dict:{key:value}
    key：必须是不可变类型tuple int string
    无序
"""
a={'a':1,'b':2}             #创建格式
a=dict(name="meng",age=18)
#b={(1,2,[1,2]),2} #会报错 key即使是元组 里边也不能包含可变对象

a['age']=3                  #可以被原地修改
a['phone']='iphoneXR'       #添加操作
a['city']='ShenYang'
a.update({'city':'Benxi'})  #key值相同会覆盖

b=a.copy()                   #浅拷贝
c=b.pop('name')              #删除元素 同时抛出值
c=b.pop('sdsdf','error')     #如果元素不存在 抛出设定值
del b['phone']               #删除字典元素
b.clear()                    #清空字典

print 'aa' in a              #判断键值存在
print b.has_key('city')

b=a.keys()                   #返回列表
c=a.values()
c=a.items()

b=a.get('city','error')
#a=b.get('ssddfdf','error')    #如果空返回 设定值
 
"""
homework
"""
ainfo={'ab':'liming','ac':20}
ainfo.update({'sex':'man','age':20})
ainfo['sex']='man'
ainfo['age']=20
print ainfo.keys()[0:2]
print ainfo.values()[0:2]
#del ainfo['ab']
#ainfo.pop('ab')
print ainfo['ac']
print ainfo.get('ac')
