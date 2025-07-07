import json
data = {
    "name": "中国",
    "province": [{
        "name": "黑龙江",
        "cities": {
            "city": ["哈尔滨", "大庆"]
        }
    }, {
        "name": "广东",
        "cities": {
            "city": ["广州", "深圳", "珠海"]
        }
    }, {
        "name": "台湾",
        "cities": {
            "city": ["台北", "高雄"]
        }
    }, {
        "name": "新疆",
        "cities": {
            "city": ["乌鲁木齐"]
        }
    }]
}
print(data)
print(type(data))

# 1.序列化
# json.dumps()：将Python中的字典或列表对象序列化为json字符串
# 注意：ensure_ascii的默认只未True，表示对中文进行编码，如果希望中文能正常显示，则可以设置ensure_ascii为False
r1 = json.dumps(data,ensure_ascii=False)
print(r1)
print(type(r1))

# json.dump():将Python中的字典或列表对象序列化到指定的文件中
with open(r'data/city.json','w',encoding='utf-8') as f1:
    json.dump(data,f1,ensure_ascii=False)

# 2.反序列化
# json.loads()：将json字符串反序列化为Python中的字典或列表对象
r2 = json.loads(r1)
print(r2)
print(type(r2))

# json.load():将指定的文件中的json字符串反序列化为Python中的字典或列表对象
with open(r'data/city.json','r',encoding='utf-8') as f2:
    r3 = json.load(f2)
    print(r3)
    print(type(r3))




