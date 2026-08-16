#打印分割线
def print_line(a,times,row):
    """打印"""
    i=0
    while i<=row:
        print(a*times)
        i+=1
print_line("*",5,6)#要尽可能的有灵活性（多可能的使用形参）
#可以看成一个整体
