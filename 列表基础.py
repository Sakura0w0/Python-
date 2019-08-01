# coding= utf-8
# 樱花的Python学习笔记
# 列表相关代码练习

doggirl = ['linlin', '琳琳', '琳琳2', '琳琳3', '琳琳4']
# 输出列表
print(doggirl)
# 输出列表序号为1的值
print(doggirl[0])
# 将值设置为title格式,首字母大写
print(doggirl[0].title())
# 输出倒数第1个值
print(doggirl[-1])
# 输出倒数第2个值
print(doggirl[-2])
# 将列表值与print结合输出
print(doggirl[0] + "是母狗")
# 直接修改列表的某个值
doggirl[0] = '超级母狗琳琳'
print(doggirl)
# 添加值进入列表末尾
doggirl.append('琳琳5')
print(doggirl)
# 将值从列表删除
del doggirl[-1]
print(doggirl)
# 将值插入某个位置之前
doggirl.insert(1, '插入琳琳')
print(doggirl)
# pop=弹出,使用pop将表格末尾输出
pop_doggirl = doggirl.pop()
print(doggirl)
print(pop_doggirl)
# pop弹出指定序号
doggirl.append(pop_doggirl)
pop_doggirl = doggirl.pop(0)
print(doggirl)
print(pop_doggirl)
# 根据指定值删除列表中的值
doggirl.remove('插入琳琳')
print(doggirl)
# 使用函数 sorted() 对列表进行临时排序
sortedlist = ['Alinlin', 'Clinlin', 'Blinlin']
print(sorted(sortedlist))
sortedlist.reverse()
print(sortedlist)
# 输出列表内值的数量
print(len(sortedlist))
dognumber = (len(doggirl))
print("总共有" + str((len(doggirl))) + "只母狗")