import json


# # 将python对象转换为json字符串
# persons = [
#     {
#         'username': 'lisa',
#         'age': 18,
#         'country': '杭州'
# },
#     {
#         'username': 'hellen',
#         'age': 18,
#         'country': '北京'
#     }
# ]
# # json.dumps()函数可以把普通的列表转换成json格式
# json_str = json.dumps(persons)
# with open('person.json', 'w',encoding='utf-8') as fp:
#       # fp.write(json_str)
#     # json.dump()函数可以直接生成json文件,ensure_ascii=False命令可以存储中文
#       json.dump(persons, fp, ensure_ascii=False)

'''
把json型文件转换为python对象
'''
# 非文件的转换
# json_str = '[{"username": "lisa", "age": 18, "country": "\u676d\u5dde"},
# {"username": "hellen", "age": 18, "country": "\u5317\u4eac"}]'
# persons = json.loads(json_str)
# print(type(persons))
# print(persons)
# json文件的转换
# with open('person.json', 'r', encoding='utf-8') as fp:
#     a = json.load(fp)
#     print(type(a))
#     print(a)

# with open('古诗词.json', 'r', encoding='utf-8') as fp:
#     a = json.load(fp)
# print(type(a))