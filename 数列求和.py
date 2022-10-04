n = eval(input("输入你要前n项和"))
if n == 1:
    sum = 1
elif n > 1:
    sum = 1
    for i in range(2, n+1):
        sum += ((-1)**i)*(1/(2*i-1))

print(f"求和的结果为{sum}")
