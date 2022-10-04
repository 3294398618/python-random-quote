num = eval(input("输入弹跳次数"))
g = 10
while num > 0:
    g = g/2
    num -= 1
print(f"篮球所在高度为{g}")