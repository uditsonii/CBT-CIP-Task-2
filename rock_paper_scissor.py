import random

user_wins = 0
computer_wins = 0
draw = 0

options = ["r", "p", "s", "q"]

while True:
    user_input = input("Type r:Rock/p:Paper/s:Scissors or q:Quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    dict = {"r" : "Rock", "p" : "Paper", "s" : "Scissors"}

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
  
    computer_pick = options[random_number]

    print(f"You choose: \"{dict[user_input]}\" and Computer picked: \"{dict[computer_pick]}\".")

    if user_input == computer_pick :
        print("Match is Draw\n")
        draw += 1

    else:
        if user_input == "r" and computer_pick == "s":
           print("You Won!\n")
           user_wins += 1

        elif user_input == "p" and computer_pick == "r":
           print("You Won!\n")
           user_wins += 1

        elif user_input == "s" and computer_pick == "p":
           print("You Won!\n")
           user_wins += 1

        else:
           print("You Lost!\n")
           computer_wins += 1

print(f"The User Wins \"{user_wins}\" times.")
print(f"The Computer Wins \"{computer_wins}\" times.")
print(f"Match Draw \"{draw}\" times.")
print("Goodbye!")