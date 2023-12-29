import random

x = 1
while (x == 1):
    x = int(input("New Game(1) : \nExit(9) : \n"))
    
    if (x==9):
        print("Exited!")

    elif(x==1):
        
        randnum = random.randint(1, 100)
        userguess = None
        guesses = 0
        
        while (randnum != userguess) :
            guesses += 1
            userguess = int(input("Enter your guess : "))
            
            if (randnum == userguess) :
                print("You guessed it right :)")
            
            elif (randnum > userguess) :
                print("You guessed it wrong!, Enter larger(+) number")

            elif (randnum < userguess) :
                print("You guessed it wrong!, Enter smaller(-) number")

        print(f"You guess the number in {guesses} guesses")


        with open ("highscore.txt","r") as f:
            highscore = int(f.read())

        if(highscore > guesses):
            print("You have just broken the high score!")
            with open ("highscore.txt","w") as f:
                f.write(str(guesses))
    else:
        print("please enter the valid number!")
        x=1

print("we are out of the game")
