# coding= utf-8
# # 樱花的Python学习笔记
# # 元组相关

# 元组与列表相似,但是并非使用[]而是(),且无法对内容进行编辑
# 定义元组示例
dimensions = (1, 10)
print(dimensions[0])
print(dimensions[1])

# 属于然无法对元组进行删减,但是可以重新赋值给元组
dimenisions = (1, 10)
print(dimenisions)
dimenisions = (1, 10, 100)
print(dimenisions)

# 结合for打印元组
food = ('薯条', '汉堡', '炸鸡')
for foodlist in food:
    print(foodlist)

# 相比于列表,元组是更简单的数据结构.如果需要储存的一组值在程序的整个生命周期中是固定的话可以使用,可以使用元组


