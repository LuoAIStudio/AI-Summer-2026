#递归函数就是在函数内部调用自己（但必须要有递归出口（进行if判断，满足条件退出循环），否则会陷入死循环）
def sum_number(num):
    print(num)
    if num==1:
        return
    sum_number(num-1)#i+=1的操作一样
sum_number(4)
#可以类比于while的循环
"""
num1=0
def sum_numbers(nums):
    num1+=nums
    if nums==1:
        return(num1)
    sum_numbers(nums-1)
result=sum_numbers(3)
print(result)
"""
def sum_numbers(num):
    if num==1:
        return 1#递归出口
    temp=sum_numbers(num-1)#假设这个可以处理1加到num-1
    return temp+num
result=sum_numbers(100)
print(result)
#以下学习面向对象（oop），先做需求分析（定义类）
"""
面向对象由类与对象组成，类则决定了对象，类是设计图纸，对象是图纸生产出来的东西，类可以看作是种类
类：由属性（这个类的描述）与方法（一般是动词）组成(命名用大驼峰命名法，首字母大写)
eg:dog是类,毛发为黄色是属性,碰到家人就摇尾巴是方法
"""
#用dir可以查看这个对象（变量，函数，数据）的内置属性与方法
class Cat:#定义类
    def eat(self):#封装方法
        print("%d岁的小猫要吃鱼"%self.age)#self可以查看属性
tom=Cat()#tom变量引用了在内存中Cat类保存的地址
tom.age=1
tom.eat()
print(tom)#用16进制打印出地址
a=id(tom)
print("%x"%a)#%x则是把10进制改为了16进制输出
huahua=Cat()
huahua.age=2#增加属性
huahua.eat()
print(huahua)#证明对象在内存中的储存位置不同，是不同的对象
#用同一个类可以打造多个对象
print(dir(huahua))