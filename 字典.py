# coding= utf-8
# 樱花的Python学习笔记
# 字典相关代码练习

# 简单的字典
alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
alien_0['color'] = 'red'
print(alien_0['color'])

# 多行字典
huangchen = {
    'name': '黄晨',
    'age': '18',
    'city': 'xiamen',
    }
print(huangchen['name'])
print(huangchen['age'])
print(huangchen['city'])

# for list 字典 结合
word = {
    'print': 'print介绍',
    'if': 'if介绍',
    'for': '循环',
    }
list = ['print', 'if', 'for']
for list2 in list:
    print(list2 + ":" + word[list2])

# for循环中包含多个键
lan = {
    're': 'java',
    'sakura': 'pthon'
    }
for name, lan2 in lan.items():
    print(name + "最爱" +lan2)

# items函数 = 键与值对应
# keys函数 = 输出键
# values函数 = 输出值
for name2 in lan.keys():
    print(name2)
for name3 in lan.values():
    print(name3)

# 对照列表与字典
dengji = {
    're': 'java',
    'sakura': 'pthon'
    }
user = ['re', 'sakura', 'linlin']
for user2 in user:
    if user2 in dengji.keys():
        print(user2 + "感谢您的记录")
    else:
        print(user2 + "请尽快登记")
