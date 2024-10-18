

import random

print('\nGUESSING THE NUMBER BETWEEN 1 AND 100!')
random.seed()
randomNumber = random.randint(1,100)

guessCount = 0

while(True):
    guessCount += 1
    guessNumber = int(input('Your guess: '))

    if guessNumber == randomNumber:
        print("You are the winner!\nNumbers of predictions:",guessCount)
        break
    elif guessNumber >= randomNumber:
        print("A bit lower")
    else:
        print("A bit higher")

