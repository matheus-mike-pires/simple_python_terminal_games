import random as rd
import pandas as pd

real_board = [
['v','v','v','v', 'v', 'v', 'x'],
['v','v','v','v', 'v', 'v', 'x'],
['v','v','v','v', 'v', 'v', 'x'],
['v','v','v','v', 'v', 'v', 'x'],
['v','v','v','v', 'v', 'v', 'x']
]

shuffle_counter = 0
while shuffle_counter < 5:
    rd.shuffle(real_board[shuffle_counter])
    shuffle_counter += 1


    
display_board = [
['o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o'],
['o', 'o', 'o', 'o', 'o', 'o', 'o']
]

print('hello! This is a simple minesweeper game')
input('press any key to continue: ')
print(' ')
display_better = pd.DataFrame(display_board)
print(display_better)
print('')
print('you will now choose a block to reveal. If right, the block will turn to a V. If wrong (block = X), the entire board will be revealed and the game will be over.')
print('')
    
while True:
    print('')
    input_y = int(input('choose the y axis (0 to 4): '))
    input_x = int(input('choose the x axis (0 to 6): '))
    display_board[input_y][input_x] = 'v'
    if display_board[input_y][input_x] == real_board[input_y][input_x]:
        print('is equal')
        print('')
        display_better = pd.DataFrame(display_board)
        print(display_better)
        continue
    else:
        print('')
        print('not equal, GAME OVER!')
        print('')
        print('Board Reveal:')
        print('----------------------------------------------')
        display_better_final = pd.DataFrame(real_board)
        print(display_better_final)
        print('----------------------------------------------')
        print('')
        retry = input('Try Again? (Y/N): ').lower()
        if retry == 'y' or retry == 'yes':
            continue
        else:
            break
            
print('Thank you for playing!')
        
    
