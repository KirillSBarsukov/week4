#!/usr/bin/env python
# coding: utf-8

# In[12]:


# import random function
import random

# Get a range from 1 to 500
randomNumber = random.randint(1,500) 
# Print a promt for user
print("User! Try to guess a random number which the coputer created") 
# Make a range for rounds from 1 to 4
for indexFirst in range (1,5): 
    # Print a round number
    print("\nRound: " + str(indexFirst)) 
    # Another range for guesses from 1 to 3
    for indexSecond in range (1,4): 
        # Print a guess number
        print("Guess: " + str(indexSecond)) 
        # Get import from user
        userInput = int(input())
        # Flow control if userInput more than randomNumber print Too high
        if userInput > randomNumber:
            print("Too high");
        # Flow control if userInput less than randomNumber print Too low
        elif userInput < randomNumber:
            print("Too low")
        # Flow control if userInput equals randomNumber print Congrats message and statistics
        elif userInput == randomNumber:
            print("\nCongrats! You win!!!!")
            print("Statistics: ")
            print("Number of rounds: " + str(indexFirst))
            print("Number of guesses: " + str(indexSecond))
            print("Hurray!")
            # User break statement if user gueesrd the number
            break

# Round counter            
inderxFirst = indexFirst + 1
print("Sorry. You lose the game.") 
print("Computer number is " + str(randomNumber)) 
print("Statistics: ") 
print("Number of rounds: " + str(indexFirst)) 
print("Number of guesses: " + str(indexSecond))


# 
