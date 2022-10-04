num = eval(input("输入一个三位数字"))
a = num//100
b = (num-a*100)//10
c = num-a*100-b*10
print(f"""个位是{c}
十位是{b}
百位是{a}""")