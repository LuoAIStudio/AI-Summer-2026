#以下继续学习字符串
str1="hello"
print(str1[1])
print(str1.count("ll"))#"ll"是子字符串
print(str1.index("e"))
print(len(str1))
str2=" \t\r\n"
print(str2.isspace())#带is的都是表示判断，判断是否只有空格与转义字符
#以下是判断是否带数字
str3="(1)"
print(str3)
print(str3.isdecimal())#只能判断数字
print(str3.isnumeric())
print(str3.isdigit())
#它们不能判断小数

