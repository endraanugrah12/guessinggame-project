import random

ran = random.randint(1,10)
inp = None

while True:
    inp = input('Guess the number: ')
    inp = int(inp)
    if inp < ran:
        print("TOO SMALL!")
    elif inp > ran:
        print('TOO BIG!')
    else:
        print('YOU WIN!')
        playAgain = input('Do you want to play again? (y/n): ')
        if playAgain == 'y':
            ran = random.randint(1,10)
            inp = None
        else:
            print('Thank you for playing deez game!')
            break
        
