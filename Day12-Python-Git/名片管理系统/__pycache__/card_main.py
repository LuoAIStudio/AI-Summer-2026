#框架的搭建（1.建立名片 2.显示全部 3.修改名片 0.退出名片）
import card_tool 
while True:#使用True就可以一直循环
    card_tool.show_menu()

    action=input("选择需要操作的信息：")
    print("你选择的操作是【%s】"%action)
    if action in ["1","2","3"]:#pass关键字保证代码的正常运行
        if action=="1":
            card_tool.creat_car()
        elif action=="2":
            card_tool.show_car()
        elif action=="3":
            card_tool.index_car()
    elif action=="0":
        print("欢迎下一次使用名片管理系统")
        
        break
    else:
        print("没有这个选项，请重新输入")