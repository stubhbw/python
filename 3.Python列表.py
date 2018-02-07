"""
不要求全部元素必须是相同的数据类型
"""

a = [1, 2, 3, 4, -7, 5, 10]
print(a[0])

# 重新定义元素
a[4] = "this text"

print(a[4])
print(a)

# 重新定义元素为数组
a[2] = [-1, -2]
print(a)

# 改变C也会改变值，并不是拷贝
b = [7, 13, 15]
c = b
print(c)
c[0] = 1
print(c)

# 拷贝,创造一个新的列表,改变不会改变原来的集合
# 拷贝全部
d = b[:]
print(d)
d[0] = "改变"
print(d)
print(b)
# 拷贝,按照索引,从0-2不包含2
e = b[0:2]
print(e)
print(b)
#列表添加元素
e.append("6666")
print(e)