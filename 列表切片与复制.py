# coding= utf-8
# 樱花的Python学习笔记
# 列表切片与复制相关

# 定义player列表
players = ['RE', 'Sakura', 'Gugan', 'LinLin']

# 输出1-3序号的玩家,终止与3序号前,也就是序号2实际为第三个玩家
print(players[0:3])

# 如果没有指定第一个索引,则会从开头开始
print(players[:2])

# 如果没有指定末尾索引,则会至列表结尾
print(players[2:])

# 遍历
for player in players[1:3]:
    print(player)

# 复制,创建新列表playerlist,复制players列表的数据0-4序列(如果不设置切片则为指向其他列表而不是复制列表的值)
playerlist = players[0:4]
print(players)
print(playerlist)
playerlist.append('233')
print(playerlist)

# copy整个列表
# playerlist = players [:]

# 错误copy,实际效果为指向
# playerlist = players

