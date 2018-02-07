# 阶乘

number = eval(input("输入一个数,我帮你求阶乘:"))

product = 1
for i in range(1, number):
    product = product * (i + 1)

print(product)
