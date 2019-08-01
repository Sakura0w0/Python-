# coding= utf-8
# 樱花的Python学习笔记
# if语句相关

# 已注册用户与队列中的新用户
current_users =  ['admin', 'linlin', 're', 'sakura', 'dog']
new_users = ['Admin', 'linlin', 'new1', 'new2', 'new3']

# 将已注册用户转化为全小写的临时格式
# 下方注释掉的代码为官方示例答案
# current_users_lower = [users.lower() for users in current_users]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

# 定义新变量在新用户循环
for new_users2 in new_users:
    # 将新用户id格式全小写,并与全小写后的已注册用户进行匹配
    if new_users2.lower() in current_users_lower:
        print("该用户名已被注册")
    else:
        current_users.append(new_users2)
        print("注册成功")
# 结尾debug测试
print(current_users)