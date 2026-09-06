#现在开始学习私有属性与方法
class Women:
    def __init__(self,name):
        self.name=name
        self.__age=18
    def secret(self):
        print("%s的年龄是%d"%(self.name,self.__age))
        #私有属性与方法可以在类的里面使用
xiaohua=Women("小花")
#print(xiaohua.__age)
#在属性的前面加上__代表私有属性，是不能在外部访问的（外部访问相当于公开）
#方法的私有性同理
xiaohua.secret()
print(xiaohua._Women__age)
#私有属性并不绝对的私有，用_类名__属性名依旧可以访问它的私有属性（私有方法同理）
#以下学习面向对象的特性——继承——相同的代码的复用（以上是封装）
class Animol:
    def run(self):
        print("跑")
    def eat(self):
        print("吃")
class Dog(Animol):
    #继承了括号当中(叫做父类）的所有属性与方法，括号外叫做子类
    def bark(self):
        print("叫")
xiaohuang=Dog()
xiaohuang.run()
xiaohuang.bark()
#以上是继承的方法，还有叫做派生（Dog是Animol的派生类，Animol是Dog的基类）
#派生（继承具有传递性），想一颗树一样不断的传递下去
class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")
xiaotianquan=XiaoTianQuan()
xiaotianquan.run()
xiaotianquan.bark()
xiaotianquan.fly()
#以下学习方法的重写（当父类中的方法不满足于需求，则可以在子类中重写）
class Dog(Animol):
    def run(self):
        print("跑跑跑")
        super().run()
        #可以调用在父类中没有被覆盖的方法
小白=Dog()
小白.run()
#可以直接覆盖父类中的相同方法
#以下学习父类的私有属性与方法（一般当中子类是不能调用父类的私有属性与方法）
#想要使用私有属性与方法可以把公用方法与属性当做媒介，从而间接的使用父类的私有属性与方法










