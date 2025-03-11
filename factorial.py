n = int(input("enter number: "))
total = 0

def fact(n):
    if n <= 1:
        return n
    else:
        num = fact(n-1)
        total = num * n
        return total

fact(n)