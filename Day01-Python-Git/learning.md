# Day01 Python + Git 学习记录

日期：2026-07-08

---

# 一、今日学习目标

今天开始 AI 学习路线的第一天，主要完成环境搭建，并学习 Python 基础运行方式以及 Git 版本管理工具。

今日重点：

1. 熟悉 VS Code 开发环境
2. 创建并运行 Python 文件
3. 理解 Python 基础语法
4. 学习 Git 基础操作
5. 将本地项目同步到 GitHub

---

# 二、开发环境配置

## 1. 使用 VS Code 作为开发工具

今天使用 VS Code 编写 Python 代码。

VS Code 主要作用：

- 编写代码
- 管理项目文件
- 运行程序
- 连接 Git
- 查看终端输出


项目结构：

```
AI-Summer-2026
│
└── Day01-Python-Git
    │
    ├── day1.py
    │
    └── learning.md
```

说明：

- `.py` 文件用于保存 Python 程序
- `.md` 文件用于记录学习笔记


---

# 三、Python基础学习

## 1. Python文件运行

Python 文件以 `.py` 作为后缀。

例如：

```
day1.py
```

运行 Python 程序：

```bash
python day1.py
```


运行后，Python 会按照代码顺序执行。


---

# 四、print()函数学习


## print()作用

print() 是 Python 中最基础的输出函数。

作用：

将内容显示到控制台。


示例：

```python
print("Hello AI")
```


输出：

```
Hello AI
```


---

# 五、变量学习


变量用于保存数据。


示例：

```python
a = 2
print(a)
```


输出：

```
2
```


变量特点：

- 不需要提前声明类型
- 可以直接赋值
- 后面的值可以覆盖前面的值


例如：

```python
a = 2

a = 3

print(a)
```


输出：

```
3
```


原因：

新的赋值会覆盖旧的数据。


---

# 六、Python基础语法理解


## 1. 注释


Python使用：

```python
#
```

表示注释。


例如：

```python
# 这是一个注释

print("Hello")
```


注释不会被 Python 执行。

作用：

- 解释代码
- 方便以后阅读
- 提高代码可维护性


---

# 七、Git版本管理学习


## 1. 什么是Git？

Git是一种版本控制工具。


作用：

- 保存代码历史
- 管理代码修改
- 多人协作开发
- 防止代码丢失


简单理解：

Git 就像代码的“存档系统”。

每一次 commit 都像游戏中的保存点。


---

# 八、本地仓库和远程仓库


Git主要有两个地方：


## 1. 本地仓库

电脑中的项目。

例如：

```
D:\AI-Summer-2026
```


## 2. 远程仓库

GitHub上的代码仓库。


关系：

```
电脑本地项目
       |
       |
      Git
       |
       |
GitHub远程仓库
```


---

# 九、Git常用命令


## 1. 查看状态


命令：

```bash
git status
```


作用：

查看：

- 当前分支
- 修改文件
- 是否需要提交


---

## 2. 添加文件


命令：

```bash
git add .
```


作用：

把修改后的文件加入 Git 暂存区。


理解：

修改文件

↓

git add

↓

告诉 Git：

“我要保存这个修改”


---

## 3. 提交版本


命令：

```bash
git commit -m "说明"
```


例如：

```bash
git commit -m "完成Day01学习"
```


作用：

创建一个版本记录。


commit信息应该说明：

- 做了什么
- 修改了什么


---

## 4. 上传GitHub


命令：

```bash
git push
```


作用：

把本地提交上传到GitHub。


流程：

```
代码修改

↓

git add

↓

git commit

↓

git push

↓

GitHub保存版本
```


---

# 十、今天遇到的Git问题


## 问题1：git push失败


错误：

```
rejected non-fast-forward
```


原因：

本地代码和GitHub远程代码历史不一致。


情况：

电脑：

```
A---B
```


GitHub：

```
A---C
```


两个版本出现分叉。


Git不知道应该保留哪个版本。


---

# 十一、解决Git同步问题


## 第一步：查看状态


命令：

```bash
git status
```


发现：

本地和远程分支存在差异。


---

## 第二步：合并远程代码


执行：

```bash
git pull
```


作用：

下载GitHub上的最新代码。


---

## 第三步：完成merge


由于发生合并，需要提交：

```bash
git commit -m "merge remote changes"
```


表示：

已经完成两个版本的合并。


---

## 第四步：重新上传


执行：

```bash
git push
```


最终：

```
本地代码
      |
      |
     Git
      |
      |
 GitHub同步成功
```


---

# 十二、今天的重要收获


## Python方面：

1. 学会创建Python文件

2. 学会运行Python程序

3. 理解print()输出

4. 理解变量赋值

5. 学会使用注释


---

## Git方面：

1. 理解Git的作用

2. 掌握基本Git流程

3. 学会提交代码

4. 学会上传GitHub

5. 第一次解决Git同步问题


---

# 十三、今天形成的开发习惯


以后开发项目遵循：

```
写代码

↓

测试运行

↓

git add .

↓

git commit

↓

git push

↓

GitHub保存
```


每天学习结束：

1. 更新learning.md

2. 保存代码

3. 提交Git版本

4. 上传GitHub


---

# 十四、明日学习计划


Python基础：

- if条件判断
- for循环
- while循环
- 函数
- 小练习


目标：

能够独立完成简单Python程序。


---

# Day01总结

今天完成了从：

“不会使用开发环境”

到：

“能够创建Python项目并同步GitHub”

的重要第一步。

Git不仅是保存代码的工具，也是未来AI工程项目管理的重要基础。