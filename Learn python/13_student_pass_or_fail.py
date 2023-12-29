a=int(input('Enter your Physics marks :'))
b=int(input('Enter your Chemistry marks :'))
c=int(input('Enter your Maths marks :'))
if (a>=33):
    a=a
else :
    print('you are fail in physics')

if (b>=33):
    b=b
else :
    print('you are fail in chemistry')

if (c>=33):
    c=c
else :
    print('you are fail in maths')

x=((a+b+c)*100)/300

if(a>=33 and b>=33 and c>=33 and x>=40) :
    print('Congetulations, you are pass in exam with percentage :',x) 
elif (x<40) :
    print('You are fail in exam because your % is less than 40%')
else :
     print('You are fail in exam')