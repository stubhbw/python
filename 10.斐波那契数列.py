# 斐波那契数列 前面两个数字加起来为后面的数字

# 0,1,1,2,3,5,8,13,21,34,55

# 迭代法
def febonaqi(index):
    terms = [0, 1]
    i = 2
    while i <= index:
        terms.append(terms[i - 1] + terms[i - 2])
        i = i + 1
    return terms[index]


print(febonaqi(6))


# 递归
def fibonaqi_digui(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return (fibonaqi_digui(index - 1) +
                fibonaqi_digui(index - 2))


# 递归
def fibonaqi_digui2(index):
    # if index == 0 or index == 1:
    if index < 2:
        return index
    else:
        return (fibonaqi_digui(index - 1) +
                fibonaqi_digui(index - 2))


print(fibonaqi_digui(10))
