#BLACKJACK

import random
import time



final = "1" 
q = "2"
new_balance = 0
balance = 5000

while not final == q or balance >= 300:
    def play(balance):
        if balance < 300:
            print("game over")
            pontos = ("." , "." , ".")
            loading_countdown = 0
            for ponto in pontos:
                while loading_countdown < 100000:
                    print(ponto)
                    time.sleep(0.1)
                    loading_countdown = loading_countdown + 1
            return
        opponents_hand = [v for v in range(9, 22)]
        print(f"your balance is {balance} USD")
        bet = int(input("place your bet:"))
        while bet < 300 or bet > balance:
            print(f"minimal bet is 300 and maximum is {balance}")
            bet = int(input("place your bet:"))
        first_card = [x for x in range(1, 12)]  
        second_card = [y for y in range(1, 11)]
        print('your cards are being handed')
        pontos = ("." , "." , ".")
        loading_countdown = 0
        for ponto in pontos:
                while loading_countdown < 3:
                    print(ponto)
                    time.sleep(1)
                    loading_countdown = loading_countdown + 1
        counter_of_hands = random.choice(first_card) + random.choice(second_card)
        show_of_hands = print(f"your hand is {counter_of_hands}.")
        compare_hands = input("do you wish to draw a new card? (y/n)")
        absolute_total_in_hands = counter_of_hands + 0
        new_cards = [new for new in range (1, 12)]
        if compare_hands == "y" and absolute_total_in_hands < 21: 
            while absolute_total_in_hands < 21 and compare_hands == "y":
                new_cards_now = random.choice(new_cards)    
                absolute_total_in_hands += new_cards_now
                if absolute_total_in_hands > 21:
                 print(f"{absolute_total_in_hands} is above the limit of 21")
                 print("you lost")
                 balance = balance - bet
                 print("now your new balance is: " , balance)
                 return balance
                print(absolute_total_in_hands)
                compare_hands = input("do you wish to draw a new card? (y/n)")
        final_dispute = random.choice(opponents_hand)
        print("both hands will be compared")
        pontos = ("." , "." , ".")
        loading_countdown = 0
        for ponto in pontos:
                while loading_countdown < 3:
                    print(ponto)
                    time.sleep(1)
                    loading_countdown = loading_countdown + 1
        print(f"your hand: {absolute_total_in_hands}. opponent's hand: {final_dispute}.")
        if absolute_total_in_hands > final_dispute:
            print("you won")
            balance = balance + bet
            print("now your new balance is: " , balance)
            return balance
        if absolute_total_in_hands < final_dispute:
            print("you lost")
            balance = balance - bet              
            print("now your new balance is: " , balance)
            return balance
        if absolute_total_in_hands == final_dispute:
            print("draw")
            print("now your balance is: " , balance)
            return balance
            
  
            
    while True:
        balance = play(balance)
                
                
        
    
                