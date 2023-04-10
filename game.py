options = ["rock", "paper", "scissors"] #list of options for the computer
computerOption = random.choice(options) #This will choose a random option from your list for the computer

print("Welcome to Rock, Paper, Scissors!")
playerOption = input("Please choose rock, paper, or scissors: ").lower()

if playerOption not in options:
    print("Invalid input. Please choose rock, paper, or scissors.")
else:
    print("You chose " + playerOption + ".")
    print("The computer chose " + computerOption + ".")

    if playerOption == computerOption:
        print("It's a tie!")
    elif (playerOption == "rock" and computerOption == "scissors") or (playerOption == "paper" and computerOption == "rock") or (playerOption == "scissors" and computerOption == "paper"):
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Better luck next time!")
