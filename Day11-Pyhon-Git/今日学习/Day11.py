#以下继续学习字符串
str1="123456"
print(str1.isdecimal())#判断是否只有数字
#以下是查找与替换，方法的名称都是见名知意
str2="hello world"
print(str2.startswith("e"))#是判断以什么开头
print(str2.endswith("l"))#判断是以什么结尾
print(str2.find("eh"))#查找（不存在返回-1），rfind是从右边为0开始查找
print(str2.replace("world","python"))#替换，但没有改变实际的字符串并保存
#以下是讲文本对齐的方法
pome=["   《登黄鹤楼》",
      "   王之涣",
      "白日依山尽  ",
      "黄河入海流",
      "欲穷千里目",
      "更上一层楼"]
for pome_str in pome:
    #print("|%s|"%pome_str.center(9))
#center是居中对齐，rjust是从右对齐，ljust是从左对齐
#以下学习去除空白字符
    print(pome_str.strip())
#以下学习拆分与连接
pome1="白日依山尽  黄河入海流  欲穷千里目  更上一层楼"
pome_list=pome1.split()
print(pome_list)
#把空白字符去掉，变成一个列表
pome2=" ".join(pome1)
print(pome2)#我是使用的空格连接
#以下学习字符串的切片（开始索引，结束索引，长度），分为顺序与倒序
str1="hello world"
print(str1[2::2])
print(str1[::-1])
"""以下都可以用IPython证明
以下学习公共方法,不用导入(len,del,max,min(比较最值,字母的话是从左到右依次增大,如果是字典的话则是比较key),cmp(高级变量之间的比较)但在py3.0以上被删了）
元组与列表都可以进行切片，与*,+的操作符
在列表当中extend是把每个元素合并,append是当成一个整体合并
成员运算符(in与not in),字典的话只能判断key
for与else的一起运用,当迭代遍历的集合迭代遍历完时会执行,如果遍历的中途使用break退出循环则不会被执行
"""



