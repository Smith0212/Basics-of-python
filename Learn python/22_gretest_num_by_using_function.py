def maximum(n1, n2, n3):
    if (n1>n2 and n1>n3):
        return n1
    elif (n2>n3):
        return n2
    else :
        return n3

a=int(input("Enter the 1 number :"))
b=int(input("Enter the 2 number :"))
c=int(input("Enter the 3 number :"))
m = maximum(a, b, c)
print("the largest number is :",m)
