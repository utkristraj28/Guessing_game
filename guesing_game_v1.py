#Guess game V1 (using the conditional logic)

#from random module importing randint to give random number between 0-10 and storing it in r_num variable
from random import randint
r_num = randint(0,10)

#guess takes input from the player
guess = int(input("Guess a Number between 0 to 10: "))

#comparing r_num and player's guess and checking if the guess is correct
if guess == r_num:
    print("You Got It!!! ")
elif guess > r_num:
    print("Too High.")
elif guess < r_num:
    print("Too Low.")
else:
    print(f"{guess} is not a Valid Entry!!")