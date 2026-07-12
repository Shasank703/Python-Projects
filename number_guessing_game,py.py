#Firstly we have to import the random number between 1 to 100
import random

#We use while True because we want the game to keep running until the user decided to exit
while True:

    #randint() function is used for generated a randon integer between two numbers
    secret = random.randint(1,100)

    attempt = 10

    #The guesses list is used for store the guesses of user 
    guesses=[]

    score = 100

    #this loop is used for to run until the user not have any attempts
    while attempt>0:
        
        #Create a variable which takes input from the user
        guess = int(input("Guess the number between 1 to 100: "))

        #it helps to find the duplicate guesses
        if guess in guesses:
            
            print("You already guess this")
            continue
        #it helps to store the guesses in list
        guesses.append(guess)
        
        #We have to compare the users value
        if guess>secret:
            print("Number is too high,Please guess lower number")
            score-=10

        elif guess<secret:
            print("Number is too low,Please guess higher number")
            score-=10

        else:
            print("Correct Number")
            break
        

        attempt-=1
        
    print("Your score is",score)
    if score>=70:
        print("You won")
    else:
        print("You lost")
    print("game over")
    print("Your Guesses: ",guesses)
        
    play=input("Do you want to play this again? (yes/no)")
    
    if play=="no":
        break


                    
                    
