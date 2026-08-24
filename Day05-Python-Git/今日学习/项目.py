#以下是elif的使用
holidayName=input("输入节日：")
if holidayName=="情人节":
    print("送玫瑰花")
elif holidayName=="平安夜":
    print("送苹果")
elif holidayName=="元旦":
    print("送汤圆")
else:
    print("节日快乐")
#以下做一个小项目，石头剪刀布
player=input("输入你要出的石头剪刀布：")
computer="剪刀"#目前没有学随机数，只能手动改
if ((player=="布" and computer=="石头") 
        or (player=="石头" and computer=="剪刀") #加一个小括号可以分行写，看起来更加的简便
        or (player=="剪刀" and computer=="布")):#再加一个Tab键是为了方便代码的阅读
    
    print("player胜利了")
elif player==computer:
#这个写复杂了(player=="布" and computer=="布") or (player=="石头" and computer=="石头") or (player=="剪刀" and computer=="剪刀"):
    print("你们是平局")
else:
    print("computer胜利了")