total = 0 
x = -123

if x < 0:
    x = x * -1

    while x != 0:
        mod = x % 10
        x = x // 10
        total = total * 10 + mod
    print(total * -1)

else:
    while x != 0:
        mod = x % 10
        x = x // 10
        total = total * 10 + mod

    print(total)