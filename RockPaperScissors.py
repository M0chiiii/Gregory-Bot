import random

number_of_matches = 0
best_of = 3
user_wins = 0
computer_wins = 0
winner = ""
win_best_of = False

while True:

    number_of_matches+=1

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    user_action = input("Enter a choice - rock, paper, or scissors: ")

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action != "rock" and user_action != "paper" and user_action != "scissors":
        user_action = input("Invalid input: not rock, paper, or scissors.")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_wins += 1
        else:
            print("Paper covers rock! You lose.")
            computer_wins += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_wins += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_wins += 1
    else: #user_action == scissors
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_wins += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_wins += 1


    if user_wins > (computer_wins + best_of - 1):
        winner = True
        win_best_of = True
        break
    elif (user_wins + best_of - 1) < computer_wins:
        winner = False
        win_best_of = True
        break
    else:
        play_again = input("play again - yes or no:")
        if play_again == "no":
            break

if user_wins > computer_wins:
    winner = "user"
elif user_wins < computer_wins:
    winner = "computer"

if win_best_of:
    if winner == "user":
      print("You win in a match of best of ",best_of," with ",user_wins," wins.")
    elif not winner == "computer":
        print("The computer wins in a match of best of ",best_of," with ",computer_wins," wins.")
    else:
        print("You played ",number_of_matches, " matches and tied with the computer.")
else:
    if winner == "user":
        print("You win ",user_wins," times in ",number_of_matches," matches.")
    elif not winner == "computer":
        print("The computer wins ",user_wins," times in ",number_of_matches,"matches.")
    else:
        print("You played ",number_of_matches," matches and tied with the computer.")