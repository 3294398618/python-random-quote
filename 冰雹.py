n = eval(input("输入一个数"))
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(n, end="  ")

