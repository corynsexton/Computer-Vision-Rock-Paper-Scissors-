import random                                                                       # Import random module                                               

rps_choices = ["rock", "paper", "scissors"]                                         # List for computer to select choice from
             
def get_computer_choice():                                                          # Creates a function to generate a computer choice for game
    computer_choice = random.choice(rps_choices)                                    # Using random module to select a random choice from list
    print(f"Comp choice: {computer_choice}")                                        # Prints computer's coice
    return computer_choice                                                          # Returns computer's choice from function
    

def get_user_choice():                                                              # Creates a function to generate user's choice                        
    user_choice = input("Rock, Paper, Scissors? ").lower()                          # Asks user to enter a choice and uses lower method to make all lower case 

    if user_choice not in rps_choices:                                              # Ensures user's choice is in our list of options
        print("Invalid input. Please choose Rock, Paper or Scissors. Try again!")   # Tells user choice is invalid and to try again
        get_user_choice()
    else:
        print(f"User guess: {user_choice}")                                         # Prints user's choice
        return user_choice                                                          # Returns user's choice from function


def get_winner(computer_choice, user_choice):                                       # Creates a function to determine who wins                  

    if computer_choice == user_choice:                                              # Ensures same choices will result in a tie
        print(f"It's a tie!")

    elif computer_choice == 'rock' and user_choice == 'scissors':                   # Ensures Rock beats Scissors                  
        print(f"You lose. {computer_choice} beats {user_choice}")

    elif computer_choice == 'paper' and user_choice == 'rock':                      # Ensures Paper beats Rock
        print(f"You lose. {computer_choice} beats {user_choice}")

    elif computer_choice == 'scissors' and user_choice == 'paper':                  # Ensures Scissors beats Paper
        print(f"You lose. {computer_choice} beats {user_choice}")

    else:
        print(f"You win! {user_choice} beats {computer_choice}")                    # Ensures user wins if computer does not


def play():                                                                         # Creates function to allow game to play
    user_choice = get_user_choice()                                                 
    computer_choice = get_computer_choice()                                                                                                             
    get_winner(computer_choice, user_choice)                                        # Calls get_winner function with computer choice and user choice passed in
 
play()
