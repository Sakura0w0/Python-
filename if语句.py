# coding= utf-8
# 樱花的Python学习笔记
# if语句相关

# 赋值RBQ列表,循环输出,当为linlin时输出linlin是肉便器否则输出RBQ名字
rbqs = ['linlin', 'baihu', 're']
for rbq in rbqs:
    if rbq == 'linlin':
        print(rbq.upper() + "是肉便器")
    else:
        print(rbq)

# 条件测试
car = 'b'
if car != 'A':
    print("car不是A")
else:
    print("car是A")

# and可以同时检测多个条件,需要都满足
ageA = 21
ageB = 22
if ageA == 21 and ageB == 22:
    print("都对")

# or也可以同时检测多个条件,满足任一就可以
ageC = 23
ageD = 24
if ageC == 23 or ageD == 23:
    print("都对")

# 检测列表or元组是否包含
listA = ['A', 'B', 'C']
if 'A' in listA:
    print("listA包含A")
# 检测列表or元组是否不包含
if 'D' not in listA:
    print("listA不包含A")

# 最简单的if语句
if ageA == 21:
    print(ageA)

#5-3训练
alien_color = ['red', 'green', 'yellow']
if 'green' in alien_color:
    print("你获得了5点")

# 5-4训练
alienA = 'red'
if alienA == 'green':
    print("你击杀了外星人并获得了5点分数")
else:
    print("你击杀了外星人获得了10点分数")

# 5-5训练
alienB = 'red'
if alienB == 'green':
    print("你击杀了外星人并获得了5点分数")
elif alienB == 'yellow':
    print("你击杀了外星人并获得了10点分数")
elif alienB == 'red':
    print("你击杀了外星人并获得了15点分数")

# 5-6训练,多条件判断
age = 13
if age < 2:
    print("是个婴儿")
elif age < 4:
    print("正在学习走路")
elif age < 13:
    print("儿童")
elif age < 19:
    print("青少年")
elif age < 64:
    print("成年人")
elif age >= 65:
    print("老年人")

# 5-7训练,检测列表 (做了优化,使用for循环而不是一个个检测)
food = ['薯条', '汉堡', '麻辣烫']
for food2 in food:
    if food2 in food:
        print("樱花爱吃" + food2)

# 5-9 练习,检测空用户
#user = ['admin', 'linlin', 're', 'sakura', 'dog']
#user = []
#for loginuser in user:
#    if loginuser == 'admin':
#        print(loginuser + "欢迎回来")
#    elif loginuser != 'admin':
#        print(loginuser + "登陆成功")
#    print("请确保有用户")
user = []
if user:
    for username in user:
        if username == 'admin':
            print("欢迎回来管理员!")
        else:
            print(username + "欢迎登陆")
else:
    print("错误")

# 5-11序数练习
number = []
for number in range(1,10):
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")