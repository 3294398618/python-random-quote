
n = int(input("输入一个数"))
for m in range(2, n):
    if n % m == 0:
        print(f'{n}不是素数')
        break
else:
    print(f"{n}是素数")