#摆放家具,先根据需求创建类（不同之间类创造的对象，可以把一个对象放在另一个对象中）
class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '"%s"的占地面积是：%.2f'%(self.name,self.area)
#在用类打造对象
bed=HouseItem("席梦思",6)
chest=HouseItem("衣柜",2)
table=HouseItem("餐桌",3.5)
print(table)
#创建类也像函数一样，需要保存
class House:
    def __init__(self,house_type,area):#需要从外部添加的才做形参
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.item_list=[]
    def __str__(self):
        return ("户型:%s\n面积:%.2f(剩余面积:%.2f)\n家具列表:%s"
                %(self.house_type,self.area,
                  self.free_area,self.item_list))
    def add_item(self,item):
        if item.area>self.free_area:
            print("%s的面积过大,无法放入到房子当中"%item)
            return
        else:
            self.item_list.append(item.name)
            print("添加家具名称为:%s"%item)
            self.free_area-=item.area
            
my_house=House("两室一厅",70)
my_house.add_item(bed)
my_house.add_item(table)
print(my_house)
#士兵突击（一个对象的属性可以是另一个类创建的对象）
class Gun:
    def __init__(self,model):
        self.model=model
        self.bullet_count=0
    def add_bullet(self,count):
        self.bullet_count+=count
    def shoot(self):
        if self.bullet_count<=0:
            print("%s型号枪里面没有子弹,请装填子弹"%self.modle)
        else:
            self.bullet_count-=1
            print("发射成功，%s型号的子弹里还剩下%d"%(self.model,self.bullet_count))
ak47=Gun("ak47")
#ak47.add_bullet(7)
#ak47.shoot()
class Soldier:
    def __init__(self,name):
        self.name=name
        self.Gun=None#不知道用什么初始值时用None
    def fire(self):
        if self.Gun is None:
            print("%s还没有枪"%self.name)
            return
        else:
            self.Gun.add_bullet(9)
            self.Gun.shoot()
            print("%s拿着%s冲锋"%(self.name,self.Gun.model))
小明=Soldier("小明")
小明.Gun=ak47
小明.fire()
print(小明.Gun.model)
#is（身份运算符）可以判断内存地址是否相同，两个变量是否引用同一个地址，一般用在None中
#==是判断是否相同
