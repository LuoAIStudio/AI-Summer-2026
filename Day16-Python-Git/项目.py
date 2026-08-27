#小明爱跑步
class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return "%s的体重是%.2f"%(self.name,self.weight)
    def eat(self):
        print("%s爱贪吃"%self.name)
        self.weight+=1
    def run(self):
        print("%s爱跑步"%self.name)
        self.weight-=0.5
xiaojie=Person("小杰",60)
xiaojie.eat()
xiaojie.run()
print(xiaojie)
#方法可以影响属性
xiaomei=Person("小美",50)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
#使用相同的类打造的不同对象，它们之间没有影响
#摆放家具










