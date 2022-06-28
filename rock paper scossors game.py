import random


while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rack, paper, scissor ?: ")
        if player == computer:
            print('computer: ', computer)
            print('player: ', player)
            print("Tie")
        elif player == "rock":
            if computer == "scissors":
                print('computer: ', computer)
                print('player: ', player)
                print("You Win!")
            elif computer == 'paper':
                print('computer: ', computer)
                print('player: ', player)
                print("You Lose!")
        elif player == "scissors":
            if computer == "paper":
                print('computer: ', computer)
                print('player: ', player)
                print("You Win!")
            elif computer == 'rock':
                print('computer: ', computer)
                print('player: ', player)
                print("You Win!")
        elif player == "paper":
            if computer == "scissors":
                print('computer: ', computer)
                print('player: ', player)
                print("You Win!")
            elif computer == 'rock':
                print('computer: ', computer)
                print('player: ', player)
                print("You Lose!")

    p = input('Play again:(y/n) ').lower()
    if (p != 'y'):
        break
