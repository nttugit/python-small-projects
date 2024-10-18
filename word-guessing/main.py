import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
result  =random.choice(words) 
limit = 7
guessTimes = 0

# print(result)
print(f'YOU HAVE {limit} TIMES TO GUESS A WORD IN THE LIST BELOW:\n',words)

while guessTimes < limit:
    guessTimes += 1
    guessWord = input('Enter your guess: ')
    print('Your guess: ',guessWord)
    if(guessWord == result):
        print('You win')
        break


if(guessTimes >= limit):
    print('You lose. The result is',result)


    