# Day14 Python 学习记录

日期：2026-08-25

---

# 一、今日学习目标

学习函数进阶：函数返回多个值、参数传递的本质、缺省参数、多值参数与拆包。

---

# 二、函数返回多个值

## 1. 用元组返回多个结果

```python
def measure():
    print("测量开始")
    wetness = 40
    temp = 34
    print("测量结束")
    return temp, wetness    # 小括号可以省略，本质是返回元组

result = measure()
print(result)               # (34, 40)
```

## 2. 用多个变量接收（解包）

```python
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
```

- 变量的个数与返回值的个数一致

---

# 三、交换两个变量的值

```python
a = 6
b = 100
a, b = b, a    # 不需要第三个变量，Python 特有写法
print(a)       # 100
print(b)       # 6
```

---

# 四、函数参数对实参的影响（重要）

## 1. 函数内部赋值不影响外部实参

```python
def dome(num, num_list):
    num = 100              # 重新赋值
    num_list = [1, 2, 3, 4, 5]
    print(num)
    print(num_list)

g_num = 99
g_num_list = [2, 3, 4, 5, 6]
dome(g_num, g_num_list)
print(g_num)        # 99    不受影响
print(g_num_list)   # [2,3,4,5,6]  不受影响
```

## 2. 用方法修改可变类型会影响外部

```python
def dome1(num_list1):
    num_list1.append(0)     # 方法修改
    print(num_list1)

num_list2 = [1, 2, 3, 4]
dome1(num_list2)
print(num_list2)    # [1,2,3,4,0]  外部也被修改！
```

## 3. 列表的 += 相当于 extend

```python
def dome3(num_list3):
    num_list3 += num_list3
    print(num_list3)

list3 = [1, 2, 3]
dome3(list3)
print(list3)        # [1,2,3,1,2,3]  会影响外部
```

---

# 五、缺省参数（默认参数）

## 1. 什么是缺省参数

- 缺省参数就是**方法的默认值**，像 `sort()` 默认升序

```python
gl_num = [3, 5, 1, 2, 5, 6, 7, 8]
gl_num.sort()              # 默认升序
gl_num.sort(reverse=True)  # 要降序必须写 reverse=True
```

## 2. 自定义缺省参数

```python
def print_info(name, gender=True):
    g_gender = "男生"
    if not gender:
        g_gender = "女生"
    print("%s是%s" % (name, g_gender))

print_info("张华", False)   # 张华是女生
```

## 3. 规则

- 把最常见的值作为缺省参数
- **缺省参数必须定义在参数列表的末尾**
- 调用多个缺省参数时，要**点名**修改哪个参数

---

# 六、多值参数

## 1. `*` 接收元组，`**` 接收字典

```python
def dome4(num4, *nums, **name):
    print(num4)     # 1
    print(nums)     # (2, 3, 4, 5, 6)
    print(name)     # {'name': '张三', 'age': '18'}

dome4(1, 2, 3, 4, 5, 6, name="张三", age="18")
```

## 2. 练习：可变参数求和

```python
def sum_numbers(*args):
    a = 0
    for b in args:
        a += b
    return a

print(sum_numbers(1, 2, 3, 4, 5, 6))    # 21
```

---

# 七、元组与字典的拆包

- 在实参中，用 `*` 拆元组、用 `**` 拆字典
- 拆包与多值参数正好配合使用

---

# 八、今天的重要收获

1. 函数可以用元组返回多个结果，用多个变量接收（解包）
2. 掌握了 Python 特有的 `a, b = b, a` 交换写法
3. **搞懂了函数参数对实参的影响**：赋值不影响，方法修改可变类型会影响——这是理解 Python 的关键
4. 会用缺省参数简化调用，知道它必须放在参数末尾
5. 会用 `*args` / `**kwargs` 接收任意数量的参数

---

# 九、遇到的问题

（如实记录今天卡住的地方……）

---

# 十、明日计划

（示例：开始学习面向对象——类与对象 class / __init__ / self）
