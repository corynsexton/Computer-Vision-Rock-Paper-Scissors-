import random                                                                           # Import random module                                               
             
def get_computer_choice():                                                              # Creates a function to generate a computer choice for game
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])                      # Using random module to select a random choice from list                                      
    print(f"Comp choice: {computer_choice}")                                            # Prints computer's choice
    return computer_choice                                                              # Returns computer's choice from function                                                  
    

def get_user_choice():                                                                  # Creates a function to generate user's choice  
    while True:
        user_choice = input("Rock, Paper, Scissors? ")                                  # Asks user to enter a choice                                                                          
        if user_choice in ["Rock", "Paper", "Scissors"]:                                # Ensures user's choice is in list of options
            print(f"User guess: {user_choice}")                                         # Prints user's choice
            return user_choice                                                          # Returns user's chioice if valid guess
        else:
            print("Invalid input. Please choose Rock, Paper or Scissors. Try again!")   # Tells user choice is invalid and to try again


def get_winner(computer_choice, user_choice):                                           # Creates a function to determine who wins                  

    if computer_choice == user_choice:                                                  # Ensures same choices will result in a tie
        print("It is a tie!")

    elif computer_choice == 'Rock' and user_choice == 'Scissors':                       # Ensures Rock beats Scissors                  
        print("You lost")

    elif computer_choice == 'Paper' and user_choice == 'Rock':                          # Ensures Paper beats Rock
        print("You lost")

    elif computer_choice == 'Scissors' and user_choice == 'Paper':                      # Ensures Scissors beats Paper
        print("You lost")

    else:
        print("You won")                                                               # Ensures user wins if computer does not


def play():                                                                             # Creates function to allow game to play
    user_choice = get_user_choice()                                                 
    computer_choice = get_computer_choice()                                                                                                             
    get_winner(computer_choice, user_choice)                                            # Calls get_winner function with computer choice and user choice passed in
 
play()
