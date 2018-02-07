# 异常的捕获

try:
    raise NameError('hhehehe')
    print(hello)
    f = open('abc.txt')
except IOError as msg:
    print(msg)
except NameError as msg:
    print(msg)
finally:
    print('123')
