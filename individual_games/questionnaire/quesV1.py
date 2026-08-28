#Questionnaire game
import json as js
import os

# 1. first, I shall present all of the individual elements necessary for this game to run

    #1.1. SCIENCE QUESTIONS
questions_scie = [
    ('What is the chemical symbol for gold?: ') , 
    ('Which planet has the most moons in the solar system?: ') , 
    ('What is the largest organ in the human body?: ') , 
    ('What gas do plants primarily absorb during photosynthesis?: ')
]

options_scie = [
        ('a. Ag  b. Au c. Fe d. Gd'),
        ('a. Jupiter b. Saturn c. Uranus d. Neptune'),
        ('a. Liver b. Brain c. Skin d. Lungs'),
        ('a. Oxygen b. Nitrogen c. Hydrogen d. Carbon dioxide')

]

awnsers_scie = (('b'), ('b'),('c'),('d'))

guesses_scie = []
score_scie = 0
max_score_scie = len(awnsers_scie) * 100

            
    #1.2. GEOGRAPHY QUESTIONS
            
questions_geo = [
    ('What is the most recent country to be recognized?: ') , 
    ('Which is the largest river in south america?: ') , 
    ('Which country has the most island in the world?: ') , 
    ('What is the capital of Australia?: ')
]

options_geo = [
        ('a. Somalia  b. Equador c. South Sudan d. New Brunei'),
        ('a. Parana b. Amazon c. San Francisco d. Orinoco'),
        ('a. Indonesia b. Sweden c. Philippines d. Japan'),
        ('a. Sydney b. Melbourne c. Canberra d. Brisbane')

]

awnsers_geo = (('c'), ('b'),('b'),('c'))

guesses = []
score = 0
max_score_geo = len(awnsers_geo) * 100

        
    #1.3. QUESTION MAKER

questions_mk = []

options_mk = []

awnsers_mk = []

guesses_mk = []
score_mk = 0

#In order to use JSON, I need to transform multiple lists into a single dictionary
#TAG 12345
dic_mk = []
def list_to_dic(list1, list2, list3):
    dic_mk = {
    'question' : list1 ,
    'option' : list2,
    'awnser' : list3
            } 
    print(dic_mk)
    name_of_file = input('choose the name of your file: ')
    with open(f"{name_of_file}.json", "w") as file:
        js.dump(dic_mk, file)
    return dic_mk 
    
dic_mk = []
def list_to_dic2(list1, list2, list3):
    dic_mk = {
    'question' : list1 ,
    'option' : list2,
    'awnser' : list3
            } 
    print(dic_mk)
#dic_mk = list_to_dic(questions_mk, options_mk, awnsers_mk) 
    
#now, I must make and save the awnsers in a json file

def question_maker(questions_mk, options_mk, awnsers_mk, guesses_mk, retry, score):
        print('welcome to the question maker function!')
        print('first, you will create a question. Then, you will make 4 possible options. At the end, you will write the awnser')
        process_of_mk_qs = ' '
        while process_of_mk_qs != 's': 
            qst_mk = input('make your question: ')
            print('for the options, write them as --- a. option A ,  b. option B , c. option C , d. option D --- ')
            print('for instance: a. Somalia  b. Equador c. South Sudan d. New Brunei')
            opt_mk = input('make 4 possible awnsers: ')
            asw_mk = input('now, type in the correct awnser: ')
            questions_mk.append(qst_mk)
            options_mk.append(opt_mk)
            awnsers_mk.append(asw_mk)
            process_of_mk_qs = input('press S to save changes and proceed to the game ; press N to make a new question: ')
            process_of_mk_qs = process_of_mk_qs.lower()
            if process_of_mk_qs == 'n':
                dic_mk = list_to_dic2(questions_mk, options_mk, awnsers_mk)
                continue
            if process_of_mk_qs == 's':
                print('before proceding to the game, we may save your questionnaire as a json file - you may replay it and share with your friends')
                dic_mk = list_to_dic(questions_mk, options_mk, awnsers_mk)
                questions_mk.clear()
                options_mk.clear()
                awnsers_mk.clear()
                dic_mk.clear()
                print('')
                main_menu()
                break
                
                
            else:
                print('not a valid option. Game will resume')
                break  
        
        
        
    #1.4. LOADING and EXTRAS
        
def loading_screen():
    print('---------------------------------------')
    print('---------------------------------------')

retry = 'r'
what_to_run = ' '
score = 0


# 2. We should also inplement a main menu where all the playing options will be displayed:
def main_menu():
    
    loading_screen()
    print('questionaire game!!!')
    loading_screen()
    print('')
    
    print('There are multiple questionaires avaible. You may also want to build your own questionaire')
    what_to_run = input('press a to play with science questions; press b to play with geography questions; press c to make your own questionaire; press d to load and fuse questionnaires: ')  
    what_to_run = what_to_run.lower() 
          
    if what_to_run == 'a':
        print('')
        play_game_scie(retry, score)
    if what_to_run == 'b':
        print('')
        play_game_geo(retry, score)
    if what_to_run == 'c':
        print('')
        question_maker(questions_mk, options_mk, awnsers_mk, guesses_mk, retry, score)
    if what_to_run == 'd':
        print('')
        import_maker_intro()
    
    
    
# 3. second, I shall prepare the structure and display that will put all of the elements into place - for Science

def play_game_scie(retry, score):
    while retry == 'r':
        question_selector_scie = 0
        
        while question_selector_scie <= len(questions_geo) - 1:
            print(questions_scie[question_selector_scie])
            print(options_scie[question_selector_scie])
            user_awns = input('what is the correct awnser?: ')
            user_awns = user_awns.lower()
            if user_awns == awnsers_scie[question_selector_scie]:
                score += 100
                print(f'correct! your curret score is {score}')
                print('')
            else:
                print('incorrect!')
                print('')
                
            question_selector_scie += 1
        
        if score == max_score_scie:
            loading_screen()
            print('PERFECT SCORE!!!!!!')
            loading_screen()
            what_to_run == 'goodbye'
            break
        
        print('')
        print(f'your total score is {score}')
        retry = input('if you wish to retry, press R. If you wish to start a new game, press N. else, press any other key to finish the program: ')
        retry = retry.lower()
        print('')
        score = 0
        
        if retry == 'r':
            continue
    
    
        if retry == 'n':
            main_menu()     
          
        else:
            print('')
            print('thank you for playing!')
            
        
# 4. third, I shall prepare the structure and display that will put all of the elements into place - for Geography

def play_game_geo(retry, score):
    while retry == 'r':
        question_selector_geo = 0
        
        while question_selector_geo <= len(questions_geo) - 1:
            print(questions_geo[question_selector_geo])
            print(options_geo[question_selector_geo])
            user_awns = input('what is the correct awnser?: ')
            user_awns = user_awns.lower()
            if user_awns == awnsers_geo[question_selector_geo]:
                score += 100
                print(f'correct! your curret score is {score}')
                print('')
            else:
                print('incorrect!')
                print('')
                
            question_selector_geo += 1
        
        if score == max_score_geo:
            loading_screen()
            print('PERFECT SCORE!!!!!!')
            loading_screen()
            what_to_run == 'goodbye'
            break
        
        print('')
        print(f'your total score is {score}')
        retry = input('if you wish to retry, press R. else, press any other key to finish the program: ')
        retry = retry.lower()
        print('')
        score = 0 
        
        if retry == 'r':
            continue
    
    
        if retry == 'n':
            main_menu()     
          
        else:
            print('')
            print('thank you for playing!')
            
#5. Now, for question making

def play_game_mk(questions_mk, options_mk, awnsers_mk, guesses_mk, retry, score):
    
    while retry == 'r':
        question_selector_mk = 0
        max_score_mk = len(awnsers_mk) * 100
        while question_selector_mk <= len(questions_mk) - 1:
            print(questions_mk[question_selector_mk])
            print(options_mk[question_selector_mk])
            user_awns = input('what is the correct awnser?: ')
            user_awns = user_awns.lower()
            if user_awns == awnsers_mk[question_selector_mk]:
                score += 100
                print(f'correct! your curret score is {score}')
                print('')
            else:
                print('incorrect!')
                print('')
                
            question_selector_mk += 1
        
        if score == max_score_mk:
            loading_screen()
            print('PERFECT SCORE!!!!!!')
            loading_screen()
            print('')
            main_menu()
            break
        
        print('')
        print(f'your total score is {score}')
        retry = input('if you wish to retry, press R. If you wish to start a new game, press N. else, press any other key to finish the program: ')
        retry = retry.lower()
        print('')
        score = 0
        
        if retry == 'r':
            continue
    
    
        if retry == 'n':
            main_menu()     
          
        else:
            print('')
            print('thank you for playing!')
            
            
# 6. I need to be able to load the JSON files and implement them into the game

    ### IMPORT MENU
def import_maker_intro():
    print('')
    print('')
    import_mk_path = input("to fuse multiple questionnaires into a single big quiz, press a. To Load a questionnaire, press b: ")
    if import_mk_path == 'a':
        import_fuser()
    if import_mk_path == 'b':
        import_maker()
        
    ### QUESTIONNAIRE OPERATION
def import_maker():
    score = 0
    print(os.listdir(locale))
    name_of_file_js = input('type in the name of the file you wish to acess (only .json files) - ex: quiz.json : ')
    with open(name_of_file_js, 'r' , encoding = 'utf-8') as f:
        loaded_data = js.load(f)
        limit_of_mks = len(loaded_data['question'])
        counter_of_mks = 0
        
        if limit_of_mks == 1:
            print('')
            print(loaded_data['question'][0])
            print(loaded_data['option'][0])
            user_awns = input('what is the correct awnser?: ')
            user_awns = user_awns.lower()
            if user_awns == loaded_data['awnser'][0]:
                print('correct!')
                print('')
                main_menu()
            else: 
                print('wrong!')
                print('')
                main_menu()
            
        if limit_of_mks > 1:
            while counter_of_mks < limit_of_mks:      
                print(loaded_data['question'][counter_of_mks])
                print(loaded_data['option'][counter_of_mks])
                verifyy = input('what is the correct awnser?: ')
                verifyy = verifyy.lower()
                if verifyy ==  loaded_data['awnser'][counter_of_mks]:
                    print('correct!')
                    score += 100
                    print('')
                else:
                    print('incorrect.')
                counter_of_mks += 1
                print('')
            
        print(f'your total score is {score}')
        retry = input('If you wish to start a new game, press N. else, press any other key to finish the program: ')
        retry = retry.lower()
        print('')
        score = 0
        
        if retry == 'n':
            main_menu()     
          
        else:
            print('')
            print('thank you for playing!')
                
  ### QUESTIONAR FUSION
# TAG 12345

quest_fuser = []
opt_fuser = []
asw_fuser = []
def import_fuser():
  print(os.listdir(locale))
  fuser_ender = ' '
  while fuser_ender != 'q' and fuser_ender != 'Q': 
      name_of_file_js = input('type in the name of the file you wish to acess (only .json files): ')
      with open(name_of_file_js, 'r' , encoding = 'utf-8') as f:
          loaded_data = js.load(f)
          quest_fuser.extend(loaded_data['question'])
          opt_fuser.extend(loaded_data['option'])
          asw_fuser.extend(loaded_data['awnser'])
      fuser_ender = input('press any key to add another questionnaire. Press Q to stop and save: ')
      if fuser_ender != 'q' and fuser_ender != 'Q':
          continue
      else:
          list_to_dic(quest_fuser, opt_fuser, asw_fuser)
          break
      
      
    
        
#7. Execute the game
locale = os.getcwd()
main_menu()


