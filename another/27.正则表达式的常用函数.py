# 正则表达式的常用函数

import re

# 未编译的正则
r1 = r'\d{3,4}-?\d{8}$'
print(re.findall(r1, "010-12345678"))

# 编译的正则 效率更高
p_tel = re.compile(r1)
print(p_tel)
print(p_tel.findall('010-12345678'))

# 编译的另一种用法
# 举例 : 现在需要匹配一段字符串   csvt 不区分大小写
# re.I
csvt_re = re.compile(r'csvt', re.I)
sss = 'csvt'
print(csvt_re.findall('CsVt'))

# re的一些方法
# match() 只有被匹配数据在开头才会返回一个对象,否则为None
print(csvt_re.match('hello csvt'))
# search() 不管匹配元素在什么位置都可以找到,没有则为None
print('-------------------search')
print(csvt_re.search('hello csvt'))
print(csvt_re.search('hello csvt').group())
print(csvt_re.search('hello csvt').start())
print(csvt_re.search('hello csvt').end())
print(csvt_re.search('hello csvt').span())
# finditer() 返回一个迭代器的对象
x = csvt_re.finditer('hello csvt')
print(x)

# sub方法

