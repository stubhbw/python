# 给一个任意的列表,对列表进行排序

a = [7, 1, 3, 5, 2, 8, 0]


# 自己写的排序
def my_sort(list):
    size = len(list)
    for i in range(size):
        for j in range(size):
            if j > i:
                if list[i] > list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
    print(list)


my_sort(a)

# 插入排序法
"""从列表的第二项开始,向前比较,
如果前一项比较小就交换位置,一直到最后一个项
"""


def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i + 1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break


b = [7, 1, 3, 5, 9, 2, 3]
insertion_sort(b)
print(b)


# 插入排序法  简化

def insertion_sort_simple(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
            list[i + 1] = list[i]
            list[i] = value
            i = i - 1


b = [7, 1, 3, 5, 9, 2, 3]
insertion_sort_simple(b)
print(b)
