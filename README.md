# Computer Vision - Rock, Paper, Scissors?
## Milestone 1
I am using `.git` and GitHub to keep track of my progress whilst developing this project. To begin, I set up a GitHub Repository and called it Computer Vision - Rock, Paper, Scissors.

---

## Milestone 2
I created an image project model using a website called Teachable-Machine. Within this model, I have created 4 classes - Rock, Paper, Scissors and Nothing which will be used within the project. Each class is trained with a bunch of images showing each gesture of Rock, Paper, Scissors and lack of gesture in 'Nothing'. I have used approximately 100 images in each class to make the model more accurate. I have then exported the model which I will later use as the structure and parameters of my deep learning model.

---

## Milestone 3
This milestone is all about creating a virtual environment to work within which will be specific for this project. This project requires a number of dependencies such as `pip`, `opencv-python`, `tensorflow` and `ipykernel`.

As I am working on an M1 Pro Mac Chip, `tensorflow` was not so simple to install and required a lot more steps. Due to this, I have called my virtual environmant `tensorflow_env` so that if I am ever using `tensorflow` in the future, I can just activate this same environment.

Once everything I need had been installed and I was happy with the virtual environment I have created, I ran the following code to test that my model was working as expected.

<img width="1076" alt="RPS-Template" src="https://user-images.githubusercontent.com/117574774/212996798-aa42302c-9075-4860-9b70-11f5ab85f4d6.png">


I held the 'paper' action to the camera and as you can see from the output below, the code is working as expected as it is returning 99% Paper.

![RPS-Templete Output](https://user-images.githubusercontent.com/117574774/212996998-4623f7f8-efa9-47c0-a79e-9136b32a73ca.png)

---

## Milestone 4
Once my conda environment was set up, I begun by creating a game of Rock, Paper, Scissors in which the user would guess a gesture by manually typing it in. 

To begin, I created a list called `rps_choices` which contained all of the possible actions you could choose for the game. 

<img width="606" alt="rps_choices" src="https://user-images.githubusercontent.com/117574774/212997039-9d18a53f-68f9-4774-93d8-bed17533ab77.png">


To generate a choice for the computer, I imported the random module so that I could select one of the options at random from the list I created so that it would be different each time. I put this into a function called `get_computer_choice` which returns the computer choice and also prints what the computer choice is when called.

<img width="588" alt="get_computer_choice()" src="https://user-images.githubusercontent.com/117574774/212997080-ed2cf72d-0f82-4540-98a6-2c68d64c52a2.png">

As I have a function which returns the computer's choice, I now need one which will return the user's choice.
I use Python's built-in `input()` function to allow the user to manually type in their choice. I have also used the `lower()` function here incase the user enters any upper-case letters, it will treat them as lower-case so that it can be located in `rps_choices`.



The user's guess can be whatever they want so I have used an `if` statement which will return a message telling the user their guess is invalid if it is not found in `rps_choices`. The `while True:` in line 13 creates a loop to ensure the `input()` function will continue until a valid guess is entered by the user. Once we have got a valid guess from the user, this function will return the user's choice and also print it out.



I now need a function to compare the two guesses and determine a winner. I have called this my `get_winner` function where I am passing the `computer_choice` and `user_choice` in as arguments. I have then written code containing the classic rules of Rock, Paper, Scissors using `if`, `elif` and `else` statements where Rock beats Scissors, Scissors beats Paper, Paper beats Rock. I have also included a line here in the case of a tie.

<img width="742" alt="get_winner()" src="https://user-images.githubusercontent.com/117574774/212997249-bfba8876-4470-473a-a8b5-bfdcbb53c6cb.png">

To finish, I have created a `play()` function to allow the game to run. Within this function, I have made `computer_choice` and `user_choice` local variables so that they can be passed into the `get_winner` function call neatly. Then all I need to do is call `play()` to play the game.

<img width="644" alt="play()" src="https://user-images.githubusercontent.com/117574774/212997284-6641efbd-c2f1-40f9-a3e5-69243ce391b6.png">

<img width="812" alt="RPS terminal results" src="https://user-images.githubusercontent.com/117574774/212997499-37a1c3b6-9a68-4e25-803a-329bad003d6b.png">

---

## Milestone 5
The main aim of this next milestone is to improve the game so that the user can guess by making a gesture to their camera/webcam instead of typing it manually. This is where the image project model that I created in Milestone 2 will come in. 

I started by creating a class named `RPS()` so that all the methods for this game are contained within one class.

Outside of the class, I imported all of the modules/libraries I would need to use within my code such as `random`, `cv2`, `models` from `keras.models`, `numpy` and `time`. There are comments throughout my code which explains which each of these are needed for.

![imports](https://user-images.githubusercontent.com/117574774/212997597-e351aae4-0a67-4c39-975f-6b91bc6ab3d1.png)

Naturally, the first thing I done in my class was initialize the attributes by using the `__init__` magic method.

![__init__](https://user-images.githubusercontent.com/117574774/212997577-8ccc46f9-a6a7-4289-9fec-4a4cd5fa4f2c.png)

To be able to allow the user to guess via the camera, I needed a method which was going to activate their camera so that the user can make their gesture towards their webcam. I called this method `get_prediction`.
Within this method, I have used `cv2`, `numpy` and `time` modules imported from Python as mentioned earlier. In this case, the time module gives the user a 1 second window to make their gesture.
The captured frame is then resized and normalized which is then sent into a data variable ready to pass into the model created earlier in the project where a prediction is then formed as to which gesture has been made by the user.

![get_prediction](https://user-images.githubusercontent.com/117574774/212997643-9479bea3-d684-4a9c-8cc0-b8b052e7119b.png)

A countdown method was put in place to notify the user that their gesture frame is about to be captured and so this method counts down from 3 to give them time to prepare. It is called before the method to activate the camera is. This is known as a `@staticmethod` as it does not need to use any instance of the class. 

![countdown](https://user-images.githubusercontent.com/117574774/212997696-81250f8a-857e-4cfe-bc6a-3d15bd87c8dc.png)

Now we have the user's guess, we need the computer's choice of rock, paper or scissors. This is a simple method - I have used the random module just like in Milestone 4 to select a random option from `list_options`. 
You will notice there is an option `'nothing'` in `list_options`, this is specifically for the user's guess in case the user does not perform a gesture. I obviously do not want this to be an option for the computer to select so I have used index slicing here.

![computer_choice](https://user-images.githubusercontent.com/117574774/212997721-df92430a-a981-4144-ab07-418d94cbfe57.png)

The next step is to determine who wins out of the computer and user and so I created a `get_winner` method.
Again similar to Milestone 4, I have used `if`, `elif` and `else` statements here. The first condition is `if` the `get_prediction` method returns `'nothing'`, it will ask the user to guess again as it is not a valid guess.
The next `elif` and `else` conditions determine who wins or if there is a tie and adds a point onto whatever the result.

Outside of the class `RPS()`, I have created a `play(nwins)` function. This function determines the rules of the game such as how many rounds need to be won before the game is over. 
I have also added in an additional line using the built-in `input()` function to allow the pace of the game to be at the user's choice. It waits for the user to press enter before automatically running the next round.

![play(nwins)](https://user-images.githubusercontent.com/117574774/212997768-380faa47-7293-437f-b729-ee60357111a7.png)

<img width="916" alt="Enter to Continue" src="https://user-images.githubusercontent.com/117574774/212997784-d0c8a73e-d7cd-40ce-b473-e15dc0839a0e.png">
