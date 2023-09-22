import random
import os
from art import logo


    

#Deck of cards to pull from
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = input("Play a game of Black Jack? Type 'y' or 'n' ")
if start_game == 'y':
    os.system('cls') 
    print(logo)
    
    max_score = 21
    # generating the player's cards
    user_cards = []
    index1= random.randint(0, len(cards) - 1)
    index2= random.randint(0, len(cards) - 1)

    first_card =  cards[index1]
    second_card = cards[index2]
    user_cards.append(first_card)
    user_cards.append(second_card)
    u_current_score = sum(user_cards)
    if u_current_score < max_score:
        print(f"Your cards: {user_cards}, current score: {u_current_score}")
        
        #checking to see if player wants another card
        another_card = input("Do you want another card? Type 'y' or 'n' to pass")
        if another_card == 'y':
            user_cards.append(random.randint(0, len(cards)- 1))
        
        # generating the dealer's cards
        dealer_cards = []
        f_dealer_card = cards[random.randint(0, len(cards) - 1)]
        s_dealer_card = cards[random.randint(0, len(cards) - 1)]
        dealer_cards.append(f_dealer_card)
        dealer_cards.append(s_dealer_card)
        d_current_score = sum(dealer_cards)
        print(f"Dealer's first card: {dealer_cards[0]}")
        
        # Checking the final scores
        if u_current_score > d_current_score and u_current_score == max_score:
            print(f"Player wins and has black Jack. Final hands: {user_cards}\nDealer's final hand: {dealer_cards} ")
        elif u_current_score > d_current_score:
            print(f"Player wins. Final hands: {user_cards}\nDealer's final: {dealer_cards} ")
        elif u_current_score < d_current_score and d_current_score == max_score:
            print(f"Dealer wins and has black Jack. Final hands: {dealer_cards}\nUser's final hand: {user_cards} ")
        elif d_current_score > u_current_score:
            print(f"Dealer wins. Final hands: {dealer_cards}\nUser's final hands: {user_cards} ")

    
    else:
        print("Busted")
    
    
        
        
    
