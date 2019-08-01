# coding= utf-8
# 樱花的Python学习笔记
# 字典相关代码练习

# 6-7 字典包含字典并循环输出
people = {
    'sakura': {
        'name': '黄晨',
        'age': '18',
        'city': '厦门',
        },
    're':{
        'name': '冉江来',
        'age': '19',
        'city': '浙江',
        }
    }
for name, info in people.items():
    print(
        "名字: " + name,
        "年龄: " + info['age'],
        "城市: " + info['city']
    )

# 6-8 字典
pets = []
pet = {
    'name': 'petA name',
    'author': 'petA author'
    }
pets.append(pet)
pet = {
    'name': 'petB name',
    'author': 'petB author'
    }
pets.append(pet)
pet = {
    'name': 'petC name',
    'author': 'petC author'
    }
pets.append(pet)
print(pets)
for pet in pets:
    print(pet['name'] + "的数据")
    for key, value in pet.items():
        print(key +": " + value)

# 6-9
place = {
    're': ['浙江', '杭州'],
    'sakura': ['厦门', '日本']
    }
for key, place2 in place.items():
    print(key + "最喜欢的地方")
    for place3 in place2:
        print(" - " + place3)