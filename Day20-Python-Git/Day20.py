#以下学习__new__方法（为对象分配空间），从而到达单例设计模式
class MusicPlayer(object):
    def __new__(cls):
        print("分配内存空间")
        #要返回创建的空间在哪里，不然Python并不知道对象该引用哪里
        instance=super().__new__(cls)
        #用super来调用父类的方法(用变量记录，又因为__new_是静态方法，要加cls)
        return instance
    def __init__(self):
        print("对象初始化")
music1=MusicPlayer()
print(music1)
class Player(object):
    instance=None
    init_flag=False
    def __new__(cls):
        if cls.instance==None:
            cls.instance=super().__new__(cls)
        return cls.instance
    def __init__(self):
        if Player.init_flag==False:
            print("执行了初始化方法")
            Player.init_flag=True#两个等号是等于，一个等号才是赋值
        elif Player.init_flag==True:
            return
    #这种判断可以让初始化只执行一次
player1=Player()
player2=Player()
print(player1)
print(player2)
#在分配类存的时候做一个判断，如果类属性是None则先分配空间，不然直接返回已经创建的的内存空间
#以下学习异常（Python解释器运行到不能解释的语法时会停止运行，并且提出错误，这个过程称作抛出异常）
#捕获异常并学习如何处理不同的异常
try:
    #不确定的代码是否能执行
    num=int(input("请输入整数:"))
    result=8/num
    print(result)
except(ValueError):
    print("请输入一个正常的整数")
except Exception as result:
    print("错误类型:%s"%result)   
    #不能完全的思考到所有错误时，来处理未知错误 ，一般放在最后 ，因为 很难全部错误思考完
except(ZeroDivisionError):
    print("分母不能为0")
else:
    print("没有出现错误的时候会被执行")
finally:
    print("无论是否出现错误都可以被执行")
    #
print("*"*4)
#以下学习异常的传递（当传递到主程序时还没有被处理，才会终止代码的运行）
def dome1():
    num=int(input("请输入整数:"))
    return num
def dome2():
    return dome1()
#异常可以在控制流中传递直到主程序中，所以只需要在主程序中来处理异常即可
try:
    dome2()
except Exception as result:
    print("未知错误:%s"%result)
#主动抛出异常（一般告诉用户输入的信息不对时等等的时候要抛出异常）
def password():
    num=input("请输入密码:")
    if len(num)>=5:
        return num
    else:
        #创建异常对象时可以描述这个异常是什么
        ex=Exception("请输入5位及以上长度的密码")
        raise ex
try:
    num=password()
    print(num)
except Exception as result:
    print(result)










