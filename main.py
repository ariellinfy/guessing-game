from random import randint
import sys

target = randint(int(sys.argv[1]), int(sys.argv[1]))

while True:
    try:
        guess = int(
            input(f'Guess a number between {sys.argv[1]}~{sys.argv[2]}: '))
        if int(sys.argv[1]) - 1 < guess < int(sys.argv[2]) + 1:
            if guess == target:
                print('You are a genius!')
                break
        else:
            print(f'number range from {sys.argv[1]} to {sys.argv[2]}')
    except ValueError:
        print('please enter a number')
        continue
