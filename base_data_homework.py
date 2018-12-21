#coding:gbk
import sys
import string
s="i,am,lilei"
print s[2:4]
print s.split(',')[1]
"""
replace方法 join方法 
"""

print bool("2012"==2012)

s=open("test.txt","r")
s1=s.read()
s.close()
print s1
print len(s1.decode("gbk"))
s2=s1.replace('\n','')
s3=s1.replace('2012','2013')
s4=s1.decode("gbk")[28/2:28/2+5]
print s4
s4=s1.decode("gbk")
print s4[-2:]
s5=s1[0:11]
print len(s5)
s=open("test1.py","w")
s.write(s3)
s.close()

a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s'%a.decode("gbk")
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
print sys.getrefcount("中文编程")
print sys.getrefcount("python编程")

a = "字符串拼接1"
b = "字符串拼接2"
print a+b
print ''.join([a,b])
print "{0},{1}".format(a,b)
print "%s,%s"%(a,b)
print ("%s,%s"%(a,b)).decode("gbk")[6].encode("utf-8")

a="i,am,a,boy,in,china"
ac="i,am,a,{boy},in,china".format(boy="girl")
print ac
print a.find('i')
print a.index('i')
print a.find('i',a.find('china'))
print a.rfind('i')
print a.count(',')

s=open("string_doc.txt","w")
sys.stdout=s
help(string)
s.close()
