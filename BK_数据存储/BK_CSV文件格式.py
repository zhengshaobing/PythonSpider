import csv


# headers = ['username', 'age', 'country']
# persons = [
#     {
#            'username': 'lisa',
#             'age': 18,
#             'country': '杭州'
#     },
#      {
#             'username': 'hellen',
#             'age': 18,
#             'country': '北京'
#         }
# ]


# def read_csv_demo1():
#     with open('stock.csv', 'r', encoding='utf-8') as fp:
#         # reader是一个迭代器,遍历这个迭代器，返回值是一个字典
#         reader = csv.reader(fp)
#         for x in reader:
#             # 次处x的类型是列表
#             print(type(x))
#
#
# def read_csv_demo2():
#     with open('stock.csv', 'r', encoding='utf-8') as fp:
#         # 使用DictReader创建的reader对象,不会包含标题那行的数据
#         # reader是一个迭代器,遍历这个迭代器，返回值是一个字典
#         reader = csv.DictReader(fp)
#         for x in reader:
#             value = {'name': x['secShortName'], 'volume': x['turnoverVol']}
#             print(value)


# def write_csv_demo1():
#     with open('classrom.csv','w', encoding='utf-8') as fp:
#         writer = csv.writer(fp)
#         writer.writerow(headers)
#         writer.writerows(persons)


# def write_csv_demo2():
#     with open('classroom.csv', 'w', encoding='utf-8') as fp:
#         writer = csv.DictWriter(fp,headers)
#         # 写入表头数据时要掉用writer.writeheader()方法
#         writer.writeheader()
#         writer.writerows(persons)
#
# if __name__ == '__main__':
    # read_csv_demo1()
    # read_csv_demo2()
    # write_csv_demo1()
    # write_csv_demo2()
# with open('古诗词.csv', 'r', encoding='utf-8') as fp:
#     a = csv.DictReader(fp)
#     for x in a:
#         print(x)
