#To play the hangman game, keep the hangman_words.py in the same directory as HangmainV1.py. 'from hangman_words import words' should do the job. Also, feel free to add words to the hangman_words

import random as rd

from hangman_words import words


test = ['anaconda']

hangman = {0: [('      '), ('       '), ('       ')], 1: [('  o  '),('       '), ('       ')], 2: [('  o  '), ('  |    '), ('       ')], 3:[('  o  '), ('--|   '), ('       ')],  4:[('  o  '), ('--|-- '), ('       ')], 5: [('  o  '), ('--|-- '), ('./    ')], 6:[('  o  '), ('--|-- '), ('./ \\.  ')]}

print('hangman game')
print()
mistake_counter = 0

selected = rd.choice(words)
word_counter = ['_ '] 
display = word_counter * len(selected)
print(*display)
print()

while mistake_counter < 6:
    user_input = input('type in a letter: ')
    while len(user_input)>1:
        print()
        print('just a single letter!')
        print()
        user_input = input('type in a letter: ').lower()   
    if user_input not in selected:
        mistake_counter += 1
        print()
        for hanged in hangman:
                print('******')
                print(hangman[mistake_counter][0])
                print(hangman[mistake_counter][1])
                print(hangman[mistake_counter][2])
                print('******')
                print()
                break
        print('wrong awnser!')
        print()
        print()
        print(*display)
        print()
    else:
        print()
        for i in range(len(selected)):
            if selected[i] == user_input:
                display[i] = user_input
     
        
        print(*display)
        print()
                
    if '_ ' not in display:
        print('victory!')
        break
        
if mistake_counter == 6:
    print()
    print(f'the right word was {selected}. Game over!')
        
print()
print('thank you for playing! ')  

    
