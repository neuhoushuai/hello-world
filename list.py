#coding:"utf-8"
import math
a=[1,2,3,4,5,6,7]
"""
����������Ƕ�ס��ɱ����� 
"""
a[0:4:1] 
a[-1:-4:-1] #��������
a[1:]#Ĭ������
a[1::2]#����2����

"""
����б�
"""
b=[4,5,6]
c=a+b #�½��б�
print id(a)
a.append(4) #ԭ��ĩβ�������Ԫ��
print id(a)
a.insert(1,[1,2])
print a
a.extend(b) #��b�е�ÿ��Ԫ�ض���ӵ��б���
print a


"""
�޸�Ԫ��
"""
A=[1,2,3]
A[0]="����" #�����gbk�����ģ�������
print A

"""
ɾ���б�Ԫ��
"""

a=[2,3,4,5]
del a[0]
a.remove(3) #ɾ����һ��ƥ�䣬û�еĻ��׳��쳣
print a
print a.pop() #ɾ�����һ��

"""
�ж�Ԫ���Ƿ����б���
"""
a=[1,2,3,4,5]
print 3 in a
print 4 not in a

"""
�б��Ƶ�ʽ
[exp for iter_var in iterable if cond_exp]
iterable�����������ɵ�����ÿ�ε����ŵ�iter_var��
exp��iter_var�е�����
"""
print [math.pow(x,2) for x in range(1,11) if x%2==0]

"""
���򣿣�
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
