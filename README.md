## 1. Computer Vision Milestone 2: Creating a system that detects whether the user is showing rock, paper or scissors to a camera


### Task1: In this milestone, a computer vision model was trained on a dataset featuring images of rock, paper, scissors and the nothing class. Each class contained approximately 800+ examples to allow the model to have a better generalization accuracy when making predictions. After the model was trained, it was exported into a keras.h5 file and stored so that it can be later implemented into a python application in the other milestones.


## 2. Computer Vision Milestone 3: Installing dependencies for mac OS

### Task 1: Before continuing with the rest of the project, a major prequisite was to install packages for mac computers in a virtual environment called tensorflow-env. Once the new env and its packages were ready, the exported model script from task 1 was run in a jupyter notebook within the tensorflow-env environment.


## 3. Computer Vision Milestone 4: Creating a rock, paper and scissors game

### Task 1: two new functions were made to build the foundations for the rps game. The first function {get_computer_choice} would pick a random choice between rock, paper and scissors and return the choice. The second function {get_user_choice} prompts the user to enter rock, paper or scissors and then return the user choice.

### Task 2: The two functions from task 1 were wrapped within another function called get_winner. This function takes two arg; computer_choice and user_choice. Using a series of if and elif statements, the function would return the winner based on the choice made by the computer and the user.

### Task 3: Now that the foundations for the rps game have been build, all the preceding functions are now put together under one function called play. Within this function the get_user_choice and get_computer_choice are called and passed onto the get_winner function, which then prints out the winner. When the {play()} function is run, the game should automatically begin by asking the user to pick between rock, paper and scissors. This input is then compared with the value returned from get_user_choice using the get_winner function. The game then prints out 'you won' if the user wins, 'you tied' if the user ties, and finall, 'you lose' if the user loses.



