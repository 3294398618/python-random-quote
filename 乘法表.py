#for i in range(1, 10):
#    for j in range(1, i+1):
#        print('{}x{}={}\t'.format(j, i, i*j), end='')
#    print()

i = 1
j = 1

while i < 10:
    while j < i + 1:
        print("{}*{}={}\t".format(j, i, i*j), end=" ")
    j += 1
i += 1
