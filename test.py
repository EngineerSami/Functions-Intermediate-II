def fact(n):
    if n == 0 :
        return 0
    return n + fact(n - 1)
i=int(input('Enter the num:'))
s=fact(i)
print("Factorial of "+str(i) + " :" , str(s))