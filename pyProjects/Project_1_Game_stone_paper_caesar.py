import random
def gameWin(comp, you):

    if comp == 's' :
        if you == 'p' :
            return print("you win!!")
        elif you == 'c' :
            return print("you loss")

    elif comp == 'p' :
        if you == 'c' :
            return print("you win!!")
        elif you == 's' :
            return print("you loss")

    elif comp == 'c' :
        if you == 's' :
            return print("you win!!")
        elif you == 'p' :
            return print("you loss!!")

print("computer's turn : stone(s), paper(p), caesar(c)? : ")
randNo = random.randint(1,3)
if randNo == 1 :
    comp = 's'
elif randNo == 2 :
    comp = 'p'
elif randNo == 3 :
    comp = 'c'

print(f"computer had chosed")

you = input("your turn : stone(s), paper(p), caesar(c)? : ")

print(f"computre chose {comp}")
print(f"you chose {you}")

gameWin(comp, you)

if comp == you :
    print("game is tie")

