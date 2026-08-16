#以下学习函数(就是先封装写过的独立代码，后面直接拿来用)
#封装时命名满足见名知意
def say_hello():
    """这个是函数专门使用的注释"""
    c=input("输入你的名字：")
    print("hello,",c)
say_hello()
#只有调用的时候才会解封，所以不能把调用放在定义上方。
#以下学习参数的调用
def 相加(num1,num2):#形参
    result=num1+num2
    print("%d+%d=%d"%(num1,num2,result))
    return result#函数的返回值,可以来反馈函数的结果，这个代表函数已经编写完成，不会执行以下代码
c=相加(20,30)#实参
#参数使函数变得更加灵活
print("计算结果：%d"%c)
#用变量来承接反馈的结果
#以下学习函数的嵌套调用
def test():
    print("hello world")
    say_hello()#把原来写过的函数嵌套在一个新的函数里面
test()
#使用模块中的函数（import）,为了明确使用建立两个py文件
#模块名是一种标识符，所以不能以数字开头（因为Python要识别它是数字还是名称，所以规定是这样的）
#以下学习函数高级变量类型（列表），一个变量存储多组数据
name=["张三","李四","王五"]
print(name[0])#0名称为索引，就是依次编号
#以下学习列表的常见操作
print(name.index("李四"))#确定在列表中的位置
name[2]="小明"
print(name[2])
#这是列表中的修改
#以下学习一下增加
name.append("小杰")
print(name)
#append是在末尾增加
name.insert(2,"小花")
print(name)#这里使用交互式的IPython要好一点
#insert可以在指定的位置插入数据
name1=["小刚","小姐"]
name.extend(name1)
print(name)
#extend是直接将两个列表合并（括号里的追加到另一个列表）
#以下是学列表的删除
name.remove("小姐")
print(name)
name.pop()#默认情况下把最后一个删除







