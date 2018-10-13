def countdown1(i):
    print(i)
    countdown1(i-1)
# countdown(1)

def countdown2(i):
    print(i)
    if i<=1:#基线条件
        return
    else: #递归条件
        countdown2(i-1)

a=countdown2(3)
