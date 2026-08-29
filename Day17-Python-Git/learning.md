# Day 17：面向对象 —— 对象组合（has-a / 一个对象的属性是另一个类的对象）

## 今日主题
- 一个对象的属性可以是另一个类创建的对象（**组合 / has-a 关系**）。
- 深入理解 `__str__` 与 `__repr__` 的区别。
- 常见坑：类名 vs 实例名、属性名一致性、用 `None` 做初始值。

## 项目一：房子摆放家具（House / HouseItem）
- `HouseItem`：家具对象（`name` 名称、`area` 占地面积）。
- `House`：房子对象（`house_type` 户型、`area` 面积、`free_area` 剩余面积、`item_list` 家具列表）。
- `add_item()`：判断家具面积是否超出剩余面积；没超出则放入列表并扣减剩余面积。
- 列表里放的是**家具对象**，体现"列表中可以存对象"。
- 注意：创建对象要用**对应的类**（`House(...)`），用错类（如 `HouseItem(...)`）就调用不到 `add_item`。

## 项目二：士兵突击（Gun / Soldier）—— 组合的典型例子
- `Gun`：枪对象（`model` 型号、`bullet_count` 子弹数），`add_bullet()` 装填、`shoot()` 开火。
- `Soldier`：士兵对象（`name` 姓名、`gun` 枪），`fire()` 里通过 `self.gun` 调用枪的方法。
- 关键：
  - `self.gun = None` 表示"还没有拿枪"。
  - `fire()` 先判断 `self.gun` 是否为空，再调用 `self.gun.add_bullet()` / `self.gun.shoot()`。
- 核心：**不需要把枪的方法抄进士兵类**，而是让士兵"持有"一个枪对象，再通过这个对象调用它的方法（这就是"一个对象的属性是另一个类的对象"）。

## `__str__` 与 `__repr__` 的区别
- `__str__`：`print(对象)` 或 `%s` 直接打印对象时显示的内容。
- `__repr__`：**对象放进列表/字典再打印时**，容器会对每个元素调用 `repr()`。
- 只写 `__str__`、没写 `__repr__`，把对象放进列表打印时就显示 `<__main__.Xxx object at 0x内存地址>`。
- 给类加上 `__repr__`（返回名称等），列表里就能显示成 `['席梦思']` 这样的内容。

## 容易踩的坑
1. **用错类**：`my_house = HouseItem(...)` -> 该类没有 `add_item` -> `AttributeError`。要用 `my_house = House(...)`。
2. **类名 vs 实例名**：`gun.model` 是问"类 `gun` 的类属性"（错误）；应该用 `self.gun.model`（方法内）或 `小明.gun.model`（外部）。
3. **属性名一致**：定义时写 `self.modle`，使用时也必须写 `.modle`；`modle` 和 `model` 是两个不同的名字，混用会 `AttributeError: ... has no attribute 'model'`。
4. **用 `None` 做初始值**：属性暂不确定时用 `None`，调用前要先判空，避免对 `None` 调用方法而报错。

---
*Day17 · 2026-08-28 · 项目文件：`今日学习/项目.py`*
