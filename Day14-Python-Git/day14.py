def measure():
    print("测量开始")
    wetness=40
    temp=34
    print("测量结束")
    return temp,wetness#这里的小括号可以去掉
result=measure()
print(result)
#用元组可以返回多个结果，如果当处理数据，可以用多个变量来接收(变量的个数与返回值的个数一致)
gl_temp,gl_wetness=measure()
print(gl_temp)
print(gl_wetness)
#以下是一道题
a=6
b=100
#如何在不引用新的变量的情况下，交换a与b的值
a,b=b,a#就像是一个函数用多个变量接收返回值
print(a)
print(b)
#在函数内部，针对参数的赋值语句，不会影响实参的变量（目前学习的所有数据类型）
def dome(num,num_list):
    num=100
    num_list=[1,2,3,4,5]
    print(num)
    print(num_list)
g_num=99
g_num_list=[2,3,4,5,6]
dome(g_num,g_num_list)
print(g_num)
print(g_num_list)
#不会影响到外部的实参变量
def dome1(num_list1):
    num_list1.append(0)
    print(num_list1)
num_list2=[1,2,3,4]
dome1(num_list2)
print(num_list2)
#如果是可变数据类型，在函数内部使用方法修改数据，则外部变量也会被修改
#针对于列表当中+=可以看作extend的方法
def dome3(num_list3):
    num_list3+=num_list3
    print(num_list3)
list3=[1,2,3]
dome3(list3)
print(list3)
#所以会影响到外部的全局变量
#缺省参数就是方法的默认值，像sort
gl_num=[3,5,1,2,5,6,7,8]
gl_num.sort()#默认值就是升序,如果要降序排列的话要reverse=True
print(gl_num)
def print_info(name,gender=True):#右边的参数默认值是Ture，最常见的值作为缺省参数
    g_gender="男生"
    if not g_gender:
        g_gender="女生"
    print("%s是%s"%(name,g_gender))
print_info("张华",False)
#这里是默认了gender这个参数，所以不用写gender=False,sort方法要倒序的话一定要写reverse=Ture,告诉python要改变的参数
#缺省参数要定义在末尾，调用多个缺省参数时要点名修改哪个参数
def dome4(num4,*nums,**name):
    print(num4)
    print(nums)
    print(name)
dome4(1,2,3,4,5,6,name="张三",age="18")
#当要接收多个值时，用一个*代表元组，**代表字典（名称为多值参数）
def sum_numbers(*args):
    a=0
    print(args)
    for b in args:
        a+=b
    return a
a=sum_numbers(1,2,3,4,5,6)
print(a)#一个把输入的值全部加起来的项目
#在实参当中想分配哪个为元组用*，哪个为字典用**（被称为字典与元组的拆包）

    



    
