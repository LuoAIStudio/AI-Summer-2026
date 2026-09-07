#以下学习多继承
class A:
    def test(self):
        print("test")
class B:
    def dome(self):
        print("dome")
class C(B,A):
    #还是用元组来封装父类
    pass
c=C()
c.test()
c.dome()
#如果多个父类中有相同的方法名，是以元组中最前面的父类中的方法为基准,(这种情况应该少用多继承，为了代码的方便)
print(C.__mro__)
#__mro__的方法可以来查找类的索引方法顺序
class D(object):
    pass
d=D()
print(dir(d))
#以object为基类的，是叫做新式类，dir可以查看类的属性与方法（如果没有指定基类，早Py3.默认是object）
#新式类与经典类的区别有方法的索引顺序
#以下学习多态（面向对象的第三特性）——子类对象使用相同的父类，产生不同的结果
class Dog(object):
    def __init__(self,name):
        self.name=name
    def game(self):
        print("%s爱玩飞盘"%self.name)
class XiaoTianQuan(Dog):
    def game(self):
        print("%s飞了起来"%self.name)
class Person(object):
    def __init__(self,name):
        self.name=name
    def game_with_dog(self,dog):
        print("%s和%s快乐的玩耍"%(self.name,dog.name))
        dog.game()
        #传入不同的狗对象产生不同的结果
#wangcai=Dog("旺财")
wangcai=XiaoTianQuan("旺财")
xiaoming=Person("小明")
xiaoming.game_with_dog(wangcai)
#创建出来的对象称为实例，每个对象在内存都有属于自己的空间，类是特殊对象
#所以类也有类属性与类对象（用赋值语句来创建类属性）
class Tool(object):
    count=0
    #用count的类属性来记录创建的工具数量
    @classmethod
    def show_count(cls):
        print("类创建的对象有:%d个"%cls.count)
    #这便是类方法的语法  
    def __init__(self,name):
        self.name=name
        Tool.count+=1
tool1=Tool("剪刀")
tool2=Tool("斧头")
tool3=Tool("钳子")
#print(Tool.count)
print("类创建的对象一共有:%d个"%tool1.count)
#Py先开始会查找tool1中是否有count的属性，如果没有查找类属性中是否有该属性
Tool.show_count()
#直接使用类方法就可以查询了
#以下学习静态方法（在方法中既不引用实例属性，也不引用类属性被称作为静态方法）
class E(object):
    @staticmethod
    def a():
        print("测验静态方法的语法")
E.a()#跟类方法的调用相似





