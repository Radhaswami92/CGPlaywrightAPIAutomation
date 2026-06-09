Num = int(input("Please provide the number to derive the factorial: "))
gfactorial = Num
if Num == 0:
    gfactorial = 1
else:
    for i in range(Num, 1, -1):
        Num = Num - 1
        gfactorial = gfactorial * Num
print(gfactorial)


