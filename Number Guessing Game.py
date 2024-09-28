# Import necessary modules
import random
import math

# Get user input for the lower and upper limits
lower_limit = int(input("Enter The Lower Limit: "))
upper_limit = int(input("Enter The Upper Limit: "))

# Generate a random number within the specified range
x = random.randint(lower_limit, upper_limit)

# Calculate the maximum number of chances based on the range
total_chances = math.ceil(math.log(upper_limit - lower_limit + 1, 2))

# Display the number of chances to the user
print("\n\tYou've only", total_chances, "chances to guess the number!\n")

# Initialize variables for counting attempts and tracking success
count = 0
flag = False

# Start the guessing loop
while count < total_chances:
    count += 1
    guess = int(input("Your Guess: "))

    # Check if the guess matches the random number
    if guess == x:
        print("Congratulations! You did it in", count, "tries")
        flag = True
        break
    elif x < guess:
        print("You guessed too high!")
        print()
    elif x > guess:
        print("You guessed too low!")
        print()

# If the user didn't guess correctly, reveal the actual number
if not flag:
    print("\nThe actual number was", x)
    print("\tBetter Luck Next Time!")

        
