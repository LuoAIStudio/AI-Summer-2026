#循环嵌套的示例
i=0
while i<=4:
    print("*"*(i+1))
    i+=1
#这是不用嵌套的
print("*",end="")#两个星号之间是两行之间连接的东西
print("*")
#在print后面加上end就可以避免换行,只能避免两行
print("*")
#以下是循环嵌套的思路
row=1
while row<=5:
    col=1#因为每次外部的循环中，col的赋值都是1，所以相当于它从新赋值了，所以col要在写在大循环的内部
    while col<=row:
        print("*",end="")
        col+=1
    print("")#每次不满足小的循环条件时换行
    row+=1
#了解到外循环控制行数，内循环控制每一行的个数
#以下是打造九九乘法口诀表的项目，类比于上面那个星星的的项目
row=1
while row<=9:
    col=1
    while col<=row:
        c=col*row
        print("%d*%d=%d"%(col,row,c),end="\t")
        col+=1#在同一个占位符上是有顺序的
    print("")
    row+=1
#以下学习转义字符（\t(目的是使打印出来的对整齐）转义为制表符 与\n（换行符）与\(使控制台输出双引号））
print("1\t2\t3")
print("11\t12\t13")
print("hallo \"world")
print("hallo\n world")
#换\n后面的
    

