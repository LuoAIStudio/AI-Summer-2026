#以下学习变量的命名（主要是见名知意）
#主要是用准确的英文来命名，如果有多个单词组成，单词之间可以用下划线连接，或者用首字母大写来区分。
#以下学习if的语句
age=input("请输入你的年龄：")#字符串的类型改变不要忘了
if age>=str(18):#==判断是否等于，！=判断是否不等于
#只要数据类型一样都能比较大小
    print("你已经成年了")
else:
    print("你还未成年")
#if判断打破了python的解释性语言顺序，如果成立执行带缩进的代码，如果不成立执行顶格的代码
#条件之间可以用and（都满足）,or（满足一个）,not（不满足才符合这个判断）来连接
#以下来学习elif的语句，它就是把判断的条件路径变多了，对比逻辑运算符只是让条件变复杂了
#if的嵌套是满足判断的前后关系,以下是示例
hasTicket=input("输入你是否有车票：")
if hasTicket=="有":
    print("可以进入")
    knifeLength=int(input("请输入刀的长度："))
    if knifeLength>=20:
        print("不能带入,你的刀为%03d,太长了,不能带入" %knifeLength)
    else:
        print("可以带入")
else:
    print("禁止进入")
#if的嵌套就是把n个判断嵌入一个大的判断
#以下再来学习随机数是如何处理的，它就是使用工具包里的工具（random）,所以改进一下剪刀石头布
import random
player=int(input("请输入你的石头1剪刀2布3:"))
computer=random.randint(1,3)
if ((player==1 and computer==2) 
        or (player==2 and computer==3) 
        or (player==3 and computer==1)):
    print("玩家你赢了,机器人出的%d"%computer)
elif player==computer:
    print("你们是平局")
else:
    print("机器人赢了,它出的%d"%computer)





