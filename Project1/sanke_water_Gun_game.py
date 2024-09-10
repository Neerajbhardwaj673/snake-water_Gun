import random

choices=("Snake","Water","Gun")

user=input(" Enter Your Choice (Snake,Water,Gun) :").strip().capitalize()

computer_choice = random.choice(choices)

print(f"Computer's choice: {computer_choice}")

if user==computer_choice:
    print("ITS A DRAW")

elif (user == "Snake" and computer_choice == "Water") or \
     (user == "Water" and computer_choice == "Gun") or \
     (user == "Gun" and computer_choice == "Snake"):
    print("ITS A WIN")

else:
    print(" YOU LOOSE")
      

    