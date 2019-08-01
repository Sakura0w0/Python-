# coding= utf-8
# 樱花的Python学习笔记
# 操作列表练习

# 定义列表并循环使用列表内的值
pizza = ['芝士披萨', '烤鸡皮萨', '至尊披萨']
for pizza2 in pizza:
    print("我爱吃" + pizza2)

# 打印 1-20
for value in range(1, 21):
    print(value)

# 打印1-1万
numbers = []
for numbers2 in range(1, 10001):
    numbers.append(numbers2)
print(numbers)

# 计算1-10000综合
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 列出1-20的所有奇数
for qishu in range(1, 20, 2):
    print(qishu)

# 1-30包含3的奇数列表
qishu2 = []
for qishu3 in range(3, 30, 3):
    qishu2.append(qishu3)
print(qishu2)

# 1-10的立方.再用for打印
ten = []
for ten in range(1, 11):
    ten2 = pow(ten, 3)
    # ten2 = int(ten) * int(ten) * int(ten)
    print(ten2)

# 列表解析表格,前10证书
squuares = [value2**3 for value2 in range(1, 11)]
print(squuares)