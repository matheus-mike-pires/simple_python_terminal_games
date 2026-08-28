from os import error
import random as rd
import time

print('-------------------------------------')
print('rock, paper, scizors game!')
print('-------------------------------------')

count_stuff = []
score = len(count_stuff)

def loading():
  load = ['.','.','.']
  for l in load:
    print(l)
    time.sleep(1)

def face_off(v1, v2):
    print('')
    print(f'you have chosen {v1}!')
    print('we shall compare hands!!!')
    loading()

    if v1 == v2:
      print("Draw!!!")
      main_menu()

    if v1 == 'rock' and v2 == 'scizors':
      print(f'you chose {v1}, the computer chose {v2}!!!')
      print('you won!')
      count_stuff.append('v')
      print(' ')
      print('your score is {score}')
      main_menu()
    if v1 == 'paper' and v2 == 'rock':
      print(f'you chose {v1}, the computer chose {v2}!!!')
      print('you won!')
      count_stuff.append('v')
      print(' ')
      print('your score is {score}')
      main_menu()
    if v1 == 'scizors' and v2 == 'paper':
      print(f'you chose {v1}, the computer chose {v2}!!!')
      print('you won!')
      count_stuff.append('v')
      print(' ')
      print('your score is {score}')
      main_menu()

    if v1 == 'paper' and v2 == 'scizors':
      print(f'you chose {v1}, the computer chose {v2}!!!')
      print('you lost!')
      main_menu()
    if v1 == 'rock' and v2 == 'paper':
      print(f'you chose {v1}, the computer chose {v2}!!!')
      print('you lost!')
      main_menu()
    if v1 == 'scizors' and v2 == 'rock':
      print(f'you chose {v1}, the computer chose {v2}!!!')
      print('you lost!')
      main_menu()







      print('welp!')


def main_menu():
  print('')
  game_agains = ['rock', 'paper', 'scizors']
  against = rd.choice(game_agains)
  game_you = input('press 1 for rocks, 2 for paper, 3 for scizors: ')
  while game_you.isdigit() == False:
    print('sorry, only numbers')
    game_you = input('press 1 for rocks, 2 for paper, 3 for scizors: ')
  game_you = int(game_you)
  while game_you < 1 or game_you > 3:
    print('sorry, out of range')
    try:
      game_you = int(input('press 1 for rocks, 2 for paper, 3 for scizors: '))
    except ValueError:
      print('invalid')
      main_menu()
  if game_you == 1:
    game_you = 'rock'
  if game_you == 2:
    game_you = 'paper'
  if game_you == 3:
    game_you = 'scizors'
  face_off(game_you, against)

main_menu()






















