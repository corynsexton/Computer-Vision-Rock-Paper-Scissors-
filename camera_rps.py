#ROCK-PAPER-SCISSORS GAME
 
import random                                                                               # Allows computer to select from list at random                                                                             
import cv2                                                                                  # Accesses camera
from keras.models import load_model                                                         # Keras easier to use tensorflow
import numpy as np                                                                          # Allows us to use arrays
import time                                                                                 # Uses seconds for countdown and image capturing time  


class RPS():                                                                                # Creates class for Rock, Paper, Scissors game

    def __init__ (self):                                                                    # Initializes attributes of class
        self.list_options = ['rock', 'paper', 'scissors', 'nothing']                        # List of choices for game
        self.computer_wins = 0                                                              # Game begins with 0 computer wins
        self.user_wins = 0                                                                  # Game begins with 0 user wins
        self.ties = 0                                                                       # Game begins with 0 ties                                                        
        self.model = load_model('keras_model.h5')                                           # Loads model created on Teaching-Machine
        self.cap = cv2.VideoCapture(0)                                                      # Assigns first camera available to 'cap'                     
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)                    # Image passed into array with specified height, width and number of channels
        

    @staticmethod                                                                           # Static Method - Does not use instance of class
    def countdown(t=1000):                                                                  # Counts down every 1000 milliseconds
        seconds = 3                                                                         # Countdown starts from 3 seconds
        max = 0                                                                             # Countdown stops at 0
        print("Ready?")                                                         
        while seconds > max:                                                                # Countdown down until 0
            print(seconds)                                                                  # Prints the countdown
            cv2.waitKey(t)                                                                  # Ends the countdown
            seconds -= 1                                                                    # Ensures the seconds count down -1
        print("Go!")


    def get_computer_choice(self):                                                          # Method to defind computer's choice
        computer_choice = random.choice(self.list_options[:3])                              # Selects rock, paper or scissors at random from list using index slicing
        return computer_choice                                                              # Returns computer's choice


    def get_prediction(self):
        endtime = time.time() + 1               

        while endtime > time.time(): 
            ret, frame = self.cap.read()                                                    # Takes first capture
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)   # Re-sizes image that model is asking for
            image_np = np.array(resized_frame)                                              # Turns image into a numpy array - Changes data                      
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1                    # Normalizes the image
            self.data[0] = normalized_image                                                 # Sends normalized image into data variable ready to pass to model   
            prediction = self.model.predict(self.data)                                      # Passes data to model to make a prediction 
            cv2.imshow('frame', frame) 
            max_index = np.argmax(prediction[0])                                            # Gives highest probability of action 
            user_choice = self.list_options[max_index]                                      # Gives corresponding element to the index in the list
            if cv2.waitKey(1) & 0xFF == ord('q'):                                           # Pressing 'q' closes camera window
                break                                                                       # Breaks loop
        
        return user_choice                                                                  # Returns user's choice


    def get_winner(self, computer_choice, user_choice):                                     # Defines function to determine winner
        print(f" \nComputer's choice: {computer_choice} \nYou chose: {user_choice}")        # Prints out computer and user's choice on separate lines

        if user_choice == "nothing":                                                        # If no action captured from user, allows user to try again 
            print(" \nTry having a guess!")
            self.get_prediction()

        elif computer_choice == user_choice:                                                # If two guesses are the same, results in a tie
            self.ties += 1
            print(f" \nUser Wins: {self.user_wins} \nComputer Wins: {self.computer_wins} \nTies: {self.ties}")

        elif computer_choice == 'rock' and user_choice == 'scissors' or computer_choice == 'paper' and user_choice == 'rock' or computer_choice == 'scissors' and user_choice == 'paper':
            self.computer_wins += 1                                                         # Adds one win to computer's number of wins
            print(f" \nYou've lost this round. {computer_choice} beats {user_choice}")      # States why computer has won
            print(f" \nUser Wins: {self.user_wins} \nComputer Wins: {self.computer_wins} \nTies: {self.ties}")
        
        else:
            self.user_wins += 1                                                             # Adds one win to user's number of wins
            print(f" \nYou win this round. {user_choice} beats {computer_choice}")          # States why user has won
            print(f" \nUser Wins: {self.user_wins} \nComputer Wins: {self.computer_wins} \nTies: {self.ties}")



def play(nwins):                                                                            # Function to define game rules with nwins being how many wins to win the game
    game = RPS()                                                                            # Calls RPS class
    
    while game.computer_wins < nwins and game.user_wins < nwins:                            # Runs game if computer or user not reached nwins
        game.countdown(1000)                                                                # Calls countdown method
        computer_choice = game.get_computer_choice()                                        # Calls method from RPS class to find computer's choice
        user_choice = game.get_prediction()                                                 # Calls method from RPS class to find user's choice
        game.get_winner(computer_choice, user_choice)                                       # Calls method from RPS class to determine winner
        input("  \nPress Enter to continue...")                                             # User must hit 'Enter' button to proceed to next round

    if game.computer_wins == nwins:                                                         # If computer reaches nwins, computer wins game
        print(f" \nComputer wins {nwins} round. \nUnlucky - Computer wins!")

    else:
        game.user_wins == nwins                                                             # If user reaches nwins, user wins game
        print(f" \nYou've won {nwins} rounds. \nCONGRATULATIONS - YOU WIN!")

    game.cap.release()                                                                      # Releases cap object
    cv2.destroyAllWindows()                                                                 # Destroys camera window

play(3)                                                                                     # First to 3 wins game
