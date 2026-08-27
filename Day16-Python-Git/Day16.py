class cat():
    def __init__(self,color):#不需要调用方法，只要创建了对象的瞬间就会自动执行这个定义的方法，所以就可以定义属性
        print("这是初始化方法")
        self.color=color
    def eat(self):
        print("%s的小猫爱吃鱼"%self.color)
    def __del__(self):
#__del__是临终前的广播，python是会自动销毁对象的，当没有东西引用对象在内存中的地址的话，就会触发销毁程序，在内存中释放出来，所以是没有东西指向该地址，就会触发以下代码
        print("%s的小猫将要离开了"%self.color)
    def __str__(self):
        return "我是小猫"#必须要返回字符串
xiaobai=cat("白色")#增加形参让代码变得灵活
xiaobai.eat()
print(xiaobai)#避免打印出来的是地址，使用__str__方法改变
print(id(xiaobai))#直接显示错误，没有这个对象了
#可以用__del__直接从内存中消除对象

