# while循环

# 基本循环 break打断
# else 在循环结束后调用,判断的表达式为反时,执行
x = ''
while x != 'q':
    print(True)
    x = input('请输入q结束循环:')
    if not x:
        break;
    if x == 'c':
        print('one more time~~c')
else:
    print('ending')
