x = int(input('输入一个数'))
y = 0
while x > 0:
    t = x %10
    x = x //10
    y = y*10+t

print(y)