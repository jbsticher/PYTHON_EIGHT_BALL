import random, time

while True:
    def slowSpacePrint(text, interval=0.1):
        for char in text:
            print(char + '', end='', flush=True)
            time.sleep(interval)
        print() # print two newlines at the end.
        print()
    # Prompt for a question
    slowSpacePrint('\n*** MAGIC FORTUNE BALL ***')
    time.sleep(0.5)
    slowSpacePrint('ASK ME YOUR YES/NO QUESTION TRAVELLER...')
    input('> ')
    # Display a brief reply
    replies = [
        '\nLET ME THINK ON THIS...',
        '\nAN INTERESTING QUESTION...LET ME PONDER A MOMENT....',
        '\nARE YOU SURE YOU WANT TO KNOW....?',
        '\nI SHALL CONSULT MY VISIONS....',
        '\nYOU MAY NOT LIKE THE ANSWER...',
        '\nI WILL CONSULT WITH THE ELDERS...'
    ]

    slowSpacePrint(random.choice(replies))

    # Dramatic pause
    slowSpacePrint('.' * random.randint(4, 12), 0.7)

    # Give the answer
    slowSpacePrint('I HAVE AN ANSWER...', 0.2)
    time.sleep(1)
    answers = [
        'IT IS DECIDELY SO',
        'SORRY, BUT THE ANSWER IS NO',
        'PLEASE ASK AGAIN LATER',
        'THERE IS A VERY GOOD POSSIBILITY',
        'YOU MAY RELY UPON IT',
    ]
    slowSpacePrint(random.choice(answers), 0.05)
    # Ask user if they would like to ask another question
    print("Would you like to ask another question? ('y' or 'n')\n")
    if not input('> ').lower().startswith('y'):
        break
   
print('\nThank you and best wishes traveller.\n')








