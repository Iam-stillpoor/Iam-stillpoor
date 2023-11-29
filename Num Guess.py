#1 #Guess the Number Game: Create a simple game where the user has to guess a randomly generated number within a certain range. You can use the random module to generate the number, but since you want to avoid using modules, you can write your own function to generate the random number.

import random

my_set = {-1,2,-3,4,-5,6,-7,-8,9,0,1,-2,-4,-6,-8}
random_element = int(random.choice(tuple(my_set)))
list=[1,2,3,4,5,6,7,8,9,0]
rnumber=(list.pop(random_element))

playerone=str(input("Please enter your name to continue: "))

print (f"Welcome {playerone} to guess the number.")
print ("You have to guess the number between 0 and 9 to win. Ensure to it that it is randomly selected.")
print("Enter 1.yes to continue or 0.no to stop.")

code=int(input("Enter your decision 1 or 0: "))

if (code==0):
     print("Build some courage.")
     quit()


elif (code==1):
     print("That's the spirit.",
           "Now choose the number (0-9).")
     playerinput=int(input("Here please proceed: "))
     if (playerinput==rnumber):
          print(f"Brilliant! {playerone}, you won.")

     else : print(f"Bad luck! get good retard. The number was {rnumber}")
    

else : quit()