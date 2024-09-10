import random

# Correctly define the tuple with individual strings
choices = ("Snake", "Water", "Gun")

# Take user input and ensure it's stripped of extra spaces and capitalized
user = input("Enter Your Choice (Snake, Water, Gun): ").strip().capitalize()

# Randomly select the computer's choice from the tuple
computer_choice = random.choice(choices)

# Print the computer's choice (for debugging or feedback purposes)
print(f"Computer's choice: {computer_choice}")

# Check the result of the game
if user == computer_choice:
    print("IT'S A DRAW")
elif (user == "Snake" and computer_choice == "Water") or \
     (user == "Water" and computer_choice == "Gun") or \
     (user == "Gun" and computer_choice == "Snake"):
    print("IT'S A WIN")
else:
    print("YOU LOSE")
