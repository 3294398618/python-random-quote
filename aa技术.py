a = int(input("输入你选择的a："))
n = int(input("输入你要多少次："))
s = 0
num = 0
for i in range(0, n):
    num = num*10+a
    s += num
print(s)
