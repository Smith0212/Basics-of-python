s1=int(input('Enter marks of student 1 : '))
s2=int(input('Enter marks of student 2 : '))
s3=int(input('Enter marks of student 3 : '))
s4=int(input('Enter marks of student 4 : '))
s5=int(input('Enter marks of student 5 : '))
s6=int(input('Enter marks of student 6 : '))
markslist = [s1,s2,s3,s4,s5,s6]
markslist.sort()
print(markslist)
print(sum(markslist)) #add all number of list