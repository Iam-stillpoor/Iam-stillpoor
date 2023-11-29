import time

name=str(input("Please enter your name")).title()

timestamp= time.strftime('%H:%M:%S')

hour=int(time.strftime('%H'))

print ("Local current time is",timestamp)

if hour>=0 and hour<12 :

    print ("Good morning",name)

elif hour>=12 and hour<16 :

    print ("Good afternoon",name)

elif hour>=16 and hour<20 :

    print ("Good evening",name)

else :
    print("Good night",name)

print("Have great time!")
