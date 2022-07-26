import random
import time

letterss = []
letters = []
list = ['The underground bunker was filled with chips and candy.',
        'Poison ivy grew through the fence they said was impenetrable.',
        "Mr. Montoya knows the way to the bakery even though he's never been there.",
        'This book is sure to liquefy your brain.',
        'Little Red Riding Hood decided to wear orange today.',
        'Despite multiple complications and her near-death experience',
        'Going from child, to childish, to childlike is only a matter of time.',
        'The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.',
        "There's a reason that roses have thorns.",
        'There is no better feeling than staring at a wall with closed eyes.']
print('''
 _____             _               _____          _            
/__   \_   _ _ __ (_)_ __   __ _  /__   \___  ___| |_ ___ _ __ 
  / /\/ | | | '_ \| | '_ \ / _` |   / /\/ _ \/ __| __/ _ \ '__|
 / /  | |_| | |_) | | | | | (_| |  / / |  __/\__ \ ||  __/ |   
 \/    \__, | .__/|_|_| |_|\__, |  \/   \___||___/\__\___|_|   
       |___/|_|            |___/                               
 _____                    _             _                      
/__   \___ _ __ _ __ ___ (_)_ __   __ _| |                     
  / /\/ _ \ '__| '_ ` _ \| | '_ \ / _` | |                     
 / / |  __/ |  | | | | | | | | | | (_| | |                     
 \/   \___|_|  |_| |_| |_|_|_| |_|\__,_|_|                     


''')


def welcome():
    ready = input(
        'Welcome to Typing Tester, the ultimate typing game to get your word skills on fleak!\n You will be given a sentence and will have to type it all out in a chosen time!\n If the sentence does not match you will be punished! Are you ready? (yes/no) ').lower()
    if ready == 'yes':
        pass
    elif ready == 'no':
        time.sleep(5)
        welcome()
    else:
        print('Please put yes or no.')
        welcome()


def timed(start):
    end = time.time()
    timedecision = input('Do you want a custom time (ct), or  Easy, Normal, or HARD!! ').lower()
    if timedecision == 'ct':
        switch = 1
        w = input('What is your max time? ')
    elif timedecision == 'easy':
        switch = 2
        pass
    elif timedecision == 'normal':
        switch = 3
        pass
    elif timedecision == 'hard':
        switch = 4
        pass
    else:
        print('Please put easy, normal, hard, or ct. ')
        timed(start)
    timer = int(start) - int(end)
    alteredtime = timer * -1
    print('The time you finished was ' + str(alteredtime) + ' seconds')
    if switch == 1:
        if alteredtime > int(w):
            print('You failed the test as you ran out of time!')
        else:
            print('You passed time...')
    if switch == 4:
        if alteredtime > 15:
            print('You failed the test as you ran out of time!')
        elif alteredtime < 15:
            print('You passed time...')
    if switch == 2:
        if alteredtime > 60:
            print('You failed the test as you ran out of time!')
        elif alteredtime < 60:
            print('You passed time...')

    if switch == 3:
        if alteredtime > 30:
            print('You failed the test as you ran out of time!')
        elif alteredtime < 30:
            print('You passed time...')


def match(typer):
    print('Checking Letters...')
    for letter in typer:
        letterss.append(letter)
    if letterss == letters:
        print('You passed spelling!')
    else:
        print('You failed spelling!!')


def test():
    class color:
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    sentence = random.choice(list)
    for word in sentence:
        for letter in word:
            letters.append(letter)

    print('\n')
    print(color.BOLD + sentence + color.END)
    print('\n')
    print('3')
    time.sleep(0.5)
    print('2')
    time.sleep(0.5)
    print('1')
    time.sleep(0.5)
    print('Time starts NOW!! Press enter to stop the time to see how you do!')
    start = time.time()
    print('Time started...')
    typer = input('Type here: ')
    # trying to make a system to print mispelled words
    # for words in typer:
    #         if not words in sentence:
    #             print('You misspelled '+words)
    #         else:
    #             print(words)
    timed(start)
    match(typer)
    ask()


def ask():
    letterss.clear()
    letters.clear()
    asks = input('Would you like to go again? ').lower()
    if asks == 'yes':
        test()
    elif asks == 'no':
        return
    else:
        print('Please put yes or no')
        ask()


welcome()
test()

