import random

def get_computer_choice():
    lst = ['Rock','Paper','Scissors']
    return random.choice(lst)


def get_user_choice():
    user_choice = input('Rock, Paper or Scissors')
    return user_choice


def get_winner(computer_choice, user_choice):
    if computer_choice == 'Rock' and user_choice == 'Rock':
        print('it is a tie!')
    elif computer_choice == 'Rock' and user_choice == 'Paper':
        print('You won!')
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print('You lost!')
    elif computer_choice == 'Paper' and user_choice == 'Paper':
        print('Its a tie!')
    elif computer_choice == 'Paper' and user_choice == 'Rock':
        print('You lost!')
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        print('You won!')
    elif computer_choice == 'Scissors' and user_choice == 'Scissors':
        print('Its a tie!')
    elif computer_choice == 'Scissors' and user_choice == 'Paper':
        print('You lost!')
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        print('You won!')