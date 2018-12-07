#coding=gbk
"标准模板"

new_str="这是一个全局变量"

def helloworld():
    """
    输出HelloWord函数
    @author:
    @copyright:
    """
    return "helloworld"

#程序主体
if __name__=="__main__":
    print helloworld()
    d=4
    print type(d)
    print \
          type(new_str) #语句换行
