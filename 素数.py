x = 0
m = 0
for n in range(500, 1, -1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(f"{n}是素数", end="\t ")
        m += 1
        x += 1
        if x%6 == 0:
            print(" ")
        if m==10:
            break