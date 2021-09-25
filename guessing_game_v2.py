#Guessing game V2 (using condtional statement and while loop)

#from random module importing randint to give random number between 0-10 and storing it in r_num variable
#outside the loop we are just defining guess so that we can use it inside the loop
from random import randint
r_num = randint(1,10)
guess = None

#while loop will let us guesing the number untill we find the right number
#the loop will stop when guess is equal to r_num
while guess != r_num:
    #guess will take input here so that we don't end up in a infinity looop 
    guess = int(input("Guess a number between 1-10: "))
    if guess > r_num:
        print("Guess is TOO HIGH")
    elif guess < r_num:
        print("Guess is TOO LOW")
    else:
        print("YOU WON!!")
#printing the random number        
print(r_num)