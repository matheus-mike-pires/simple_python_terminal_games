import random as rd
import time


all_slots = ['🔔','🍀','💣','🍋','🍋','🔔']
filler = '#'
money = 300

def main(money):
    print()
    print('*******************')
    print('Python Cassino')
    print('*******************')
    print()
    wait_time = input('Press any key to play ')
    run_slots(money)
            
    

def run_slots(money):
    while True:
        spin1 = rd.choice(all_slots)
        spin2 = rd.choice(all_slots)
        spin3 = rd.choice(all_slots)
        
        money -= 10
        
        print()
        
        print(f'----------------')
        print(f'----{spin1}|{filler}|{filler}----')
        print(f'----------------')
        time.sleep(1)
        
        print()
        
        print(f'----------------')
        print(f'----{spin1}|{spin2}|{filler}----')
        print(f'----------------')
        time.sleep(1)
        
        print()
        
        print(f'----------------')
        print(f'----{spin1}|{spin2}|{spin3}----')
        print(f'----------------')
        time.sleep(1)
        
        print()
        
        if spin1 == spin2 and spin2 == spin3 and spin3 == '🔔':
            print('you won 60 dollars')
            money += 60
            print(f'your wallet: {money} dollars')
            again = input('press any key to try again and q to quit: ').lower()
            if again == 'q':
                main(money)
            
                
        if spin1 == spin2 and spin2 == spin3 and spin3 == '🍋':
            print('you won 50 dollars')
            money += 50
            print(f'your wallet: {money} dollars')
            again = input('press any key to try again and q to quit: ').lower()
            if again == 'q':
                main(money)
            
        if spin1 == spin2 and spin2 == spin3 and spin3 == '🍀':
            print('JACKPOT! you won 120 dollars')
            money += 120
            print(f'your wallet: {money} dollars')
            again = input('press any key to try again and q to quit: ').lower()
            if again == 'q':
                main(money)
            
        if spin1 == spin2 and spin2 == spin3 and spin3 == '💣':
            print('Bad luck! you lost 30 dollars')
            money -= 30
            print(f'your wallet: {money} dollars')
            again = input('press any key to try again and q to quit: ').lower()
            if again == 'q':
                main(money)
            
        if spin1 != spin2 or spin2 != spin3:
            print(f'your wallet: {money} dollars')
            again = input('press any key to try again and q to quit: ').lower()
            if again == 'q':
                main(money)
            
                                    
        
    
        
    
main(money)
