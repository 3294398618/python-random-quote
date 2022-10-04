n = eval(input("输入年份"))
y = eval(input("输入月份"))

if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
    print(f"{n}年{y}月有31天")
elif y == 4 or y == 6 or y == 9 or y == 11:
    print(f"{n}年{y}月有30天")
elif y == 2:
    if n % 4 == 0 and n % 100 != 0:
        print(f"{n}年{y}月有29天")
    elif n % 400 == 0:
        print(f"{n}年{y}月有29天")
    else:
        print(f"{n}年{y}月有28天")
else:
    print("输入正确的月份")
