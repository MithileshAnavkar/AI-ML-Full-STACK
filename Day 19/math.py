from datetime import datetime

now = datetime.now()

print(now.date())
print(now.time())
print(now)
print("----------")

import random

number = random.randint(1,6)
print("random number is" , number)
print("-----------")

import random


number = random.randint(1,10)
while True:
    guess = int(input("Guess Your Number:"))
    
    if number < guess:
      print("Your guess is higher")

    elif number > guess:
       print("Your guess is lower!")

    else:
       print("Your guess is correct")
       break