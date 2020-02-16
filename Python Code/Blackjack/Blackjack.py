import math
import random     # Import Modules that the program will use
import time

balance = 100


hit_vocab = ["hit", "Hit", "h", "H"]  # List of all the things the user coult type instead of "Hit"
stand_vocab = ["Stand", "stand", "s", "S"]

print("Welcome To Blackjack! I'm the Dealer and I'll Be Your Host!")
time.sleep(2)

double_down_vocab = ["dd", "double down", "DoubleDown", "Double", "double", "DD", "Double Down", "Double down", "Dd", "Double-down", "Double-Down", "double-down"]


def deal():
    global card1
    global card2
    global dealer_card1
    global dealer_card2
    global random_card
    global random_card2
    global balance
    global cards
    random_card2 = random.choice(cards)
    random_card = random.choice(cards)
    card1 = random.choice(cards)
    card2 = random.choice(cards)  # Picking a random card from the array (cards)
    time.sleep(0.5)
    print("Your cards are", card1, "and", card2) # Will implement the (your total is) in GUI
    if card1+card2 > 21:
        print("You bust!")
        balance = balance-place_bet
    else:
        pass
    cards.remove(card1) #removing the random cards from the array so they cannot be used again this hand
    cards.remove(card2)
    dealer_card1 = random.choice(cards)
    dealer_card2 = random.choice(cards)  # Picking a random card from the array (cards) to be the dealer's card
    time.sleep(1)
    print("The Dealer has", dealer_card1, "and something else you cannot see at this time.")
    cards.remove(dealer_card1) #removing the random cards from the array so they cannot be used again this hand
    cards.remove(dealer_card2)
    time.sleep(1)
    print("Would you like to Hit, Stand, or Double-Down?")
    hit_stand_doubledown = str(input(">> "))
    if hit_stand_doubledown in hit_vocab:    # If they type anything 'in' the list hit_vocab, it will call the hit function
        hit()
    elif hit_stand_doubledown in stand_vocab:  #else if they type something in the list stand_vocab, call the stand funtion
        stand()
    elif hit_stand_doubledown in double_down_vocab:
        double_down()


def main():    # The Actual Program that has the code in it
    global balance
    global cards
    global place_bet
    cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]
    print("Please Place Your Bet! You Curently Have", balance, "points!")
    place_bet = int(input(">> "))
    if place_bet > balance:   # If you bet more than you have, it will give you this error and
        time.sleep(1)         # Ask you if you want to bet again
        print("You don't Have Enough Points!")
        time.sleep(0.5)
        main()   # Will start from the beginning of the function, and ask for another bet.
    elif place_bet == 1:
        timr.sleep(1)
        print("Sorry, but you can't bet 1!")  # Standard blackjack rules, you have to bet 2 or over.
        time.sleep(0.5)
        main()
    else:
        balance = balance-place_bet    # If you have the points, it will subtract the bet from your balance
        print("Okay, Processing...")
        time.sleep(1)
        print("You now Have", balance, "points")
        time.sleep(0.5)
        deal()


def hit():  # The hit function, if the user types "hit"
    global balance
    global cards
    global dealer_cards
    print("You hit!")
    time.sleep(0.4)
    print("You got a", random_card)
    cards.remove(random_card)
    print("You now have a", card1, "a", card2, "and a(n)", random_card)
    time.sleep(0.25)
    if card1+card2+random_card > 21:
        print("You bust! Sorry")
        print("You have", balance, "points.")
        time.sleep(0.2)
        main()
    elif card1+card2+random_card == 21:
        print("You win!")
        payout = place_bet*2
        balance = balance+payout
        time.sleep(0.2)
        print("Your balance is now", balance)
        main()
    else:
        if dealer_card1+dealer_card2 < 21:
            time.sleep(0.3)
            print("The dealer hits!")
            time.sleep(0.2)
            print("The dealer now has a", dealer_card1, dealer_card2, "and a card you cannot see at the time")
            dealer_cards = [dealer_card2, dealer_card1, random_card]
            cards.remove(random_card)
        elif dealer_card1+dealer_card2 == 17:
            pass
        else:
            print("The dealer busts! You win!")
            time.sleep(0.1)
            payout = place_bet*2
            balance = balance+payout
            time.sleep(0.2)
            print("Your balance is now", balance)
            main()
        print("Would you like to Hit, Stand, or Double-Down?")
        hit_stand_doubledown = str(input(">> "))
        if hit_stand_doubledown in hit_vocab:    # If they type anything 'in' the list hit_vocab, it will call the hit function
            hit_2()
        elif hit_stand_doubledown in stand_vocab:  #else if they type something in the list stand_vocab, call the stand funtion
            stand()
        elif hit_stand_doubledown in double_down_vocab:
            double_down_2()

def hit_2():
    global balance
    global cards
    global dealer_cards
    print("You hit!")
    time.sleep(0.4)
    print("You got a", random_card)
    time.sleep(0.2)
    cards.remove(random_card)
    print("You now have a", card1, "a", card2, "a", random_card, "and a", random_card2)
    time.sleep(0.25)
    if card1+card2+random_card > 21:
        print("You bust! Sorry")
        print("You have", balance, "points.")
        time.sleep(0.2)
        main()
    elif card1+card2+random_card+random_card2 == 21:
        player_cards = [card1+card2+random_card+random_card2]
        print("You win!")
        payout = place_bet*2
        balance = balance+payout
        time.sleep(0.2)
        print("Your balance is now", balance)
        main()
    else:
        print("Would you like to Hit, Stand, or Double-Down?")
        hit_stand_doubledown = str(input(">> "))
        if hit_stand_doubledown in hit_vocab:    # If they type anything 'in' the list hit_vocab, it will call the hit function
            hit_2()
        elif hit_stand_doubledown in stand_vocab:  #else if they type something in the list stand_vocab, call the stand funtion
            stand()
        elif hit_stand_doubledown in double_down_vocab:
            double_down_2()


def double_down():
    print("You hit!")
    time.sleep(0.4)



def stand():  # The stand function, if the user types "stand"
    global balance
    global cards
    global dealer_cards
    dealer_cards = [dealer_card2, dealer_card1, random_card]
    print("You stand!")
    time.sleep(0.4)
    dealer_cards.append(random_card)
    if dealer_cards[0]+dealer_cards[1]+dealer_cards[2] > 17:
        if dealer_cards[0]+dealer_cards[1]+dealer_cards[2] > 21:
            print("The dealer busts! You win.")
            payout = place_bet*2
            balance = balance+payout
            time.sleep(0.2)
            print("Your balance is now", balance)
            main()
        else:
            pass
    else:
        if dealer_cards[0]+dealer_cards[1]+dealer_cards[2] > player_cards:
            print("You lose!")
            time.sleep(0.1)
            main()
        elif dealer_cards[0]+dealer_cards[1]+dealer_cards[2] < player_cards:
            if player_cards < 21:
                print("you win!")
                payout = place_bet*2
                balance = balance+payout
                time.sleep(0.2)
                print("Your balance is now", balance)
                main()
            else:
                pass
        else:
            pass


main()
