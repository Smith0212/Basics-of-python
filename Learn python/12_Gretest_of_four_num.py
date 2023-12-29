from traceback import print_tb


a=int(input('Enter the 1 number :\n'))
b=int(input('Enter the 2 number :\n'))
c=int(input('Enter the 3 number :\n'))
d=int(input('Enter the 4 number :\n'))
if (a>b):
    s1=a
else :
    s1=b
if (c>d):
    s2=c
else :
    s2=d
if (s1>s2):
    print(s1, "is the gretest number")
else :
    print(s2, "is the gretest number")