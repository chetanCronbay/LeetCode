s = "bbbba"
p = ".*a*a"

i = j = 0
temp = ""
while j < len(p) or i < len(s):
    if (j < len(p) and i < len(s)) or (j < len(p) - 1 and p[j+1] == "*"):
        if i == len(s): 
            j += 2

        elif s[i] == p[j] or p[j] == ".":
            # if j == len(p) - 1 and i < len(s):
            #     print(False)
            # else:
                j += 1
                i += 1
        elif p[j] == "*" and j < len(p):
            if p[(j -1)] == ".":
                while i < len(s):
                    i += 1
            else:        
                temp = p[(j - 1)]
                if j == len(p) -1:
                    while i < len(s) and temp == s[i]:
                        i += 1
                else:
                    while i < len(s) - 1 and temp == s[i]:
                        i += 1
            j += 1

        else:
            if j < len(p):
                j += 1
            else:
                print(False)

    else:
        print(False)

print(True)