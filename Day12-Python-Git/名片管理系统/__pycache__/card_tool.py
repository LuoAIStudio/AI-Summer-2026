#显示菜单
card_list=[]#用来保存数据的总列表

def show_menu():
    print("*"*60)
    print("")
    print("欢迎使用名片管理系统")
    print("1.建立名片 2.显示全部 3.查找名片 0.退出名片系统")
    print("")
    print("*"*60)
#以下建立新增文件板块
def creat_car():
    print("-"*60)
    print("建立文件")
    #提示用户输入
    name=input("请输入名字：")
    qq=input("请输入qq:")
    email=input("请输入邮箱:")
    num=input("请输入电话号码:")
    #建立名片字典
    card_dict={"name":name,
               "qq":qq,
               "email":email,
               "num":num}
    #把一个字典的整体储存在列表当中
    card_list.append(card_dict)
    print("建立名片成功")
    print(card_list)
    #验证创建完成
    
#以下建立显示所有名片
def show_car():
    print("-"*60)
    print("显示所有名片")
    #以下是判断在列表中是否有储存的名片
    if card_list==[]:#也可以用len(card_list==0来限定)
        print("目前没有储存的名片,还请输入名片")
    else:
        for name in ["名字","QQ","邮箱","电话号码"]:
            print(name,end="\t\t")#使其排在一排，\t与空格的区别是使其变得整齐
        print("")
        print("-"*60)
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],
                                        card_dict["qq"],
                                        card_dict["email"],
                                        card_dict["num"]))#只显示字典的值，不显示key
        
#以下是搜索并修改名片
import card_tool
def index_car():
    print("-"*50)
    print("查看并修改文件")
    find_name=input("请输入要查询的名字:")
    for card_dict in card_list:
        if find_name==card_dict["name"]:
            print("找到了")
            for name in ["名字","QQ","邮箱","电话号码"]:
                print(name,end="\t\t")#使其排在一排，\t与空格的区别是使其变得整齐
            print("")
            print("-"*60)
            print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],
                                                    card_dict["qq"],
                                                    card_dict["email"],
                                                    card_dict["num"]))
            #以上就是查询名片了
            print("是否要修改名片")
            creat=input("请输入你的选择:")
            if creat=="是":
                card_tool.deal_card(card_dict)
            elif creat=="否":
                break
            else:
                print("请重新输入")
        else:
            print("没有查询到相关名字")
    
#以上就是查询文件的功能为了避免代码过于的冗长，再来定义一个函数，处理找到的名片信息
def deal_card(card_dict):
    while True:
        print("1.修改名片 2.删除名片 0.返回上一级菜单")
        card_creat=input("请输入要选择的功能：")
        if card_creat=="1":
            card_dict["name"]=input_card(card_dict["name"],"名字(回车可以不修改):")
            card_dict["qq"]=input_card(card_dict["qq"],"QQ:")
            card_dict["email"]=input_card(card_dict["email"],"邮件:")
            card_dict["num"]=input_card(card_dict["num"],"号码：")
            print("修改名片成功")
            break
        elif card_creat=="2":
            card_list.remove(card_dict)
            print("已经成功删除名片")
            break
        elif card_creat=="0":
            break
        else:
            print("没有这项功能,请重新输入")
#为了满足开发的需要，就不用input函数了，自己在开发一个函数,input如果回车的话是要修改的
def input_card(dict_value,tip_message):
    result_str=input(tip_message)
    if len(result_str)>0:
        return result_str
    else:
        return dict_value
    
        
    
    
    
    



