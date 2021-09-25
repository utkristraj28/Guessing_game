#Guessing Game V4

#from random module importing randint to give random number between 0-10 and storing it in r_num variable
#outside the loop we are just defining guess so that we can use it inside the loop
from random import randint
r_num = randint(1,10)
guess = None

#while true will let the loop go for infinity times
while True:
    guess = int(input("Guess a number between 0-10"))
    if guess < r_num:
        print("Guess is LOW")
    elif guess > r_num:
        print("Guess is HIGH")
    else:
        print("YOU WON!!")
        #play_again variable will take a string input yes or no to play the game again
        play_again = input("Want to Play Again (y/n)?").lower()
        #if play_again is yes r_num will take a random number again 
        #and guess will become none again
        if play_again == "y":
            r_num = randint(0,10)
            guess = None
        #else get out of the game and break out of the infinity loop
        else:
            print("Thank You Playing. Have a Good Day :D ")
            break