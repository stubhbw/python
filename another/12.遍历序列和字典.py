# 遍历序列和字典

# 将数据中的元素取出

# ----遍历序列
list = [1, 2, 3, 4, 5, 6, 7]
str = 'hello'
t = (1, 2, 3, 4, 5, 6, 7)
# 取出序列的值
for x in list:
    print(x)
# 取出序列的索引
for x in range(len(list)):
    print(x)
# 取出序列的值
for x in str:
    print(x)

# ----遍历字典 遍历出来的是key
dict2 = {'a': 1, 'b': 2, 'c': 3}
print(dict2)
# for x in dict:
#     print(x)
#     print(dict[x])
# ----遍历字典 同时遍历 key 和 value
big = dict2.items()
print(big)
for k, v in big:
    print(k)
    print(v)
