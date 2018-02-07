# 递归

# 普通
def factorial(number):
    product = 1
    for i in range(1, number):
        product = product * (i + 1)
    return product


# 递归
def factorial2(number):
    if number <= 1:
        return 1
    else:
        return number * factorial2(number - 1)
