# 字符串
a = "my first test string"
b = 'Another test string that i have defined'
c = "This is Hebw's String"

# 错误示范
# d = 'This is Hebw's Sting'
# 可以这样写
d = 'My favorite word is "dadsf",what is yours?'
math_string = "3+4*2"
expression_string = "a+' '+b+' tiger'"

# 字符串长度
print(len(a))
print(len(math_string))

# 字符串相加
a_with_b = a + b
print(a_with_b)
b_with_a = b + a
print(b_with_a)

# 一些字符串的函数
# 分割
b.split(" ")
print(b.split(" "))
print(b.split("t"))
# 查找某个字符的索引
print(math_string.find("*"))
# 替换
print(c.replace("i", "替换"))
# 神奇的计算,根据字符串里的内容进行计算
print(eval(math_string))
print(eval(math_string + '1'))
print(eval(expression_string))
