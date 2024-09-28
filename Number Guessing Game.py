import random
import math

lower_limit = int(input("Enter The Lower Limit : "))

upper_limit = int(input("Enter The Upper Limit : "))

x = random.randint(lower_limit,upper_limit)

total_chances = math.ceil(math.log(upper_limit - lower_limit + 1,2))

print("\n\tYou've only ", total_chances, "chances to guess the number!\n")

count = 0

flag = False

while count < total_chances:

    count += 1

    guess = int(input("Your Guess : "))

    if guess == x:
        print("Congratulations! You did it in", count , "try")
        flag = True
        break

    elif x < guess:
        print("You guessed too high!")
        print()

    elif x > guess:
        print("You guessed too low!")
        print()
if not flag:
    print("\nThe actual number was ", x)
    print("\tBetter Luck Next Time! ")

        
