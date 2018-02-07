# 循环控制
# for循环  break continue return
import time

# else 在循环结束后调用
# 当程序非正常结束时ending不会执行
s = 'hello'
for k in s:
    print(k)
    # time.sleep(1)
else:
    print("ending")
# 当break打断循环触发时不会走else
for k in s:
    print(k)
    if k == 'l':
        break;
else:
    print("ending")
# continue 跳过循环的后续代码块
for k in s:
    if k == 'l':
        continue;
    print(k)
else:
    print("ending")


# return
def ret():
    for x in 'hello':
        print(x)
        if x == 'e':
            return 1
        print('666')
    else:
        print('-----ending')


a = ret()
print(a)
