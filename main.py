import random


def play():
    player = input("Choose:'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 'c'])
    if player == computer:
        return 'It\'s a tie'

    if is_win(player, computer):
        return f'Congratulations! You won! The computer chose {computer}.'

    return f'You lost! The computer chose {computer}.'


def is_win(player, computer):
    if player == 'r' and computer == 's':
        return True
    elif player == 'p' and computer == 'r':
        return True
    elif player == 's' and computer == 'p':
        return True
    else:
        return False


loop = 'y'
while loop == 'y':
    print(play())
    loop = input('Type y to play again, otherwise type any key to quit.\n').lower()
