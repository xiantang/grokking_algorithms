x=1680
y=640
print(x%y)
print(y%x)
def DC(x,y):
    if x>y:
        x=x%y
        if x ==0:
            return y
        return x+DC(x,y)
    if x<y:
        y=y%x
        if y ==0:
            return x
        return z+DC(x,y)
print(DC(x,y))