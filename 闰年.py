for n in range(2000, 3001):
    if n % 4 == 0 and n % 100 != 0:
        print(f"{n}是闰年")
    elif n % 400 == 0:
        print(f"{n}是闰年")
    else:
        pass