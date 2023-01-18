import random

def get_computer_choice():
    lst = ['Rock','Paper','Scissors']
    return random.choice(lst)


def get_user_choice():
    user_choice = input('Rock, Paper or Scissors')
    return user_choice


