#  Random Alphabetic Selection  Generator

# You need a fair place to start in a list of alphabetical elemets
# like in a class. Don't always want to start at A. Give you your first
# selection and then you go Alphabetcally, loopin back to A after Z.
# Seeded by datetime. Not truly Random, but good enough for fun.

import random
from datetime import datetime


myNum = 0
myNum2 = 0


random.seed(datetime.now())

print("DRUM ROLL")
for x in range(100):
    print(x)
    myNum =(random.randrange(1, 27))
    print ("  ",myNum)
    myNum2 = myNum +64
    print ("     ",myNum2)
    print ("          ",chr(myNum2))

print("--------------------------------------------------------")  
print("")
print("This is your starting point!!!")
print("")
print ("                            ",chr(myNum2))
print("--------------------------------------------------------")


zz = input( "Enter")


   
