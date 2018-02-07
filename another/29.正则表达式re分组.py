# 正则表达式 re分组
import re

r1 = r'csvt.net'

a = re.findall(r1, 'csvt.net')
a = re.findall(r1, 'csvtOnet', re.S)
# 使.匹配包括换行在内的所有字符----------------------re.S
a = re.findall(r1, 'csvt\nnet', re.S)
print(a)

s = """ 
hello csvt
csvt hello
hello csvt hello
csvt hehe
"""
# 字符串多行的情况下 , 行首匹配不成功
r = r'^csvt'
print(re.findall(r, s))
# 字符串多行的情况下匹配行首,用这个-------------------re.M
print(re.findall(r, s, re.M))
# 正则多行的情况下匹配,用这个------------------------re.X


# ------------------------------------------------分组
# 举例: 匹配邮箱地址.关键是结尾的元素有几个可能
# 使用后面的括号包裹,分组.在分组中可以'或 | '等其他操作
email = r'\w{3}@\w+(\.com|\.cn)'
print(re.match(email, 'zzz@csvt.com'))
print(re.match(email, 'zzz@csvt.cn'))
print(re.match(email, 'zzz@csvt.org'))
# 当存在分组的时候,在匹配的时候会优先返回分组中的数据
print(re.findall(email, 'zzz@csvt.com'))


#
s = """hhsdj dskj hello src=csvt yes jdjsds
djhsjk src=123 yes jdsa src=234 yes
hello src=python yes ksa
"""
r1 = r'hello src=.+ yes'
print