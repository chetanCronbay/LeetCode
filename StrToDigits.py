s = "  +  413"
flag = True
trigger = False
total = []
for letter in s:
    if letter == " " and total == [] :
        pass

    elif letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9" or letter == "-" or letter == "+":
        total.append(letter)
        if letter !="-" and letter != "+":
            trigger = True
    
        if letter == "-":
            total.pop()
            if trigger == True:
                break
            flag = False
            trigger = True
            pass
        elif letter == "+":
            total.pop()
            if trigger == True:
                break
            trigger = True
            pass
    
    else:
        break

if total == [] or total == ["-"] or total == ["+"]:
    total = 0
else:
    total = int("".join(total))

if flag == False:
    total = total * -1
    if total < (-2**31):
        print(-2**31)
    else:
        print(total)
else:
    if total > (2**31 - 1):
        print(2**31 - 1)
    else:
        print(total)