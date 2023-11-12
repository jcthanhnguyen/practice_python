import random, termcolor

def hangman(word):
    hidden = list()
    for i in word:
        hidden.append('_')
    print(f'\nGuess the hidden word:\n{hidden}')
    
    lifes = 3
    guessed_list = list()
    
    while lifes != 0:
        if '_' not in hidden:
            print(termcolor.colored('\nYou have won !!!', 'yellow'))
            break
        
        if lifes > 1:
            print(termcolor.colored(f'\nYou have {lifes} lifes', 'green'))
        else:
            print(termcolor.colored(f'\nYou have {lifes} life left', 'magenta'))
        
        print(f'Guessed words: {guessed_list}')    
        guess = input('Guess a character: ')
        if guess in guessed_list:
            print('You have entered this character before')
            continue
        else: 
            guessed_list.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden[i] = guess
        else:
            lifes -= 1
        print(hidden)
        
    if lifes == 0: 
        print(termcolor.colored('\nYou have lost', 'red'))
        
        
#main
word_list = ['random', 'idiot', 'math', 'book', 'hacker', 'pentest']
print(termcolor.colored('**** Hangman Game ****', 'cyan'))
hangman(random.choice(word_list))        