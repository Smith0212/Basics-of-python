def tempreture(cel):
    return (cel * (9/5)) + 32 

a=int(input("enter the tempreture in celsius :"))
f= tempreture(a) 
print("Tempreture in the fahrenheit is :",f)