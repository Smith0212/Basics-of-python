def sum_recursive(n):
    return n + sum_recursive(n-1)

a=int(input("Enter the number :"))
s=sum_recursive(a)
print(f"Sum of the {a} number is :",s)