h = eval(input("输入身高"))
w = eval(input("输入体重"))
BMI = h/w**2
if BMI< 18.5 and BMI>0:
    print("体重过轻")
elif 18.5<BMI and BMI< 24:
    print("体重正常")
elif 24<=BMI and  BMI< 28:
    print("偏胖")
elif BMI>= 28:
    print("肥胖")
else:
    print("数据错误")