# 利用海伦公式求解三角形面积
a = eval(input("请输入第一条边的长"))
b = eval(input("请输入第二条边的长"))
c = eval(input("请输入第三条边的长"))
p = (a + b + c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
# 换完之后啊a<b<c
if a+b > c and c-b < a:
    print(f"三角形的面积是: {s}")
else:
    print("这不是一个三角形")