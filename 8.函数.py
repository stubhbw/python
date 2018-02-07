# 定义一个函数
# 函数关键字 def

# 求阶乘
def factorial(number):
    product = 1
    for i in range(1, number):
        product = product * (i + 1)
    return product


user_input = eval(input("给个数字号码"))
factor_user_input = factorial(user_input)
print(factor_user_input)
print(factorial(10))
