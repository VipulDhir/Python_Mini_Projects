import random

print("Lets play Rock, Paper, Scissors game ")

player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
if player_choice in ["rock", "paper", "scissors"]:
    print(player_choice)
else:
    print("Invalid choice. Please try again.")


computer_choice = random.choice(["rock", "paper", "scissors"])
print(computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
    print("You win!")
else:
        print("Computer wins!")