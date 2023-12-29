q=1
while q==1:
    x=input("what do you want to perform : addition(a), substrection(s), multiplication(m), divition(d), exit(e) :")
    if x == 'e' :
        break
       
    elif (x == 'a' or x == 's' or x == 'm' or x == 'd') :
        try:
            a=int(input("enter the 1 number :"))
            b=int(input("enter the 2 number :"))

            if x == 'a' :
                print(f"addition of {a} and {b} is :",a+b)
            elif  x == 's' :
                print(f"substrection of {a} and {b} is :",a-b)
            elif  x == 'm' :
                print(f"multiplication of {a} and {b} is :",a*b)
            elif  x == 'd' :
                if b == 0 :
                    print("infinite")
                else : 
                    print(f"divition of {a} and {b} is :",a/b)  
        except Exception as e :
            print ("ValueError, please enter valid number")

    else :
        print("Enter mentioned alfabate!")
                    
print ("you are exited from program!!")