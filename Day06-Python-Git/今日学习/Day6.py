#接下来来学循环，程序的三大流程有顺序，分支，循环
i=0
while i<=3:
    print("hallo word")
    i+=1#一定要修改条件，要不然会进入死循环,处理计数器
print("输出的i=%d"%i)
#以下学习赋值运算符，+=,-=（c+=a,c=c+a）,(c-=a,c=c-a),其余同理
#以下学习Python的计数方法，在大部分的程序当中，都是从0开始的
result=0
i=0
while i<=100:
    result+=i
    i+=2
print("0到100的偶数求和为%d"%result)
#以下是另一种思路来处理前100的偶数和相加
result=0
i=0
while i<=100:
    if i%2==0:#先找出前100的偶数，余数为1则是奇数相加，0为偶数相加
        result+=i#等号两边的顺序搞清楚了
    i+=1
print("0到100的偶数求和为%d"%result)
#以下学习break（满足条件，打破循环，不再执行了）与continue(是直接回到循环开始的起点）的关键字
i=0
while i<=10:
    if i==3:
        break
    i+=1
print("i的值为%d"%i)
#以下是continue的使用
i=0
while i<10:
    if i==3:
        i+=1#在上面加，因为Python是一行一行的解释
        continue#一定要修改计数值，不然会进入死循环，就是回到第32行
    print(i)
    i+=1
#以下学习循环嵌套

    

    
    




    