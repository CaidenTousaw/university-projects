from tkinter import Tk, Label, Button
import time
import random


cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]
starting_card = random.choice(cards)
starting_card2 = random.choice(cards)
new_card = random.choice(cards)
new_card2 = random.choice(cards)
dealer_card = random.choice(cards)
dealer_card2 = random.choice(cards)
dealer_card3 = random.choice(cards)
dealer_card4 =  random.choice(cards)
cards.remove(new_card)
cards.remove(starting_card)
cards.remove(starting_card2)
cards.remove(new_card2)
cards.remove(dealer_card)
cards.remove(dealer_card2)
cards.remove(dealer_card3)
cards.remove(dealer_card4)



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Blackjack - Caiden Tousaw")

        self.label = Label(master, text=starting_card)
        self.label.pack()
        self.label.place(x=460, y=480)

        self.label2 = Label(master, text=starting_card2)
        self.label2.pack()
        self.label2.place(x=500, y=480)

        self.label_dealer = Label(master, text=dealer_card)
        self.label_dealer.pack()
        self.label_dealer.place(x=460, y=80)

        self.label_dealer2 = Label(master, text="??")
        self.label_dealer2.pack()
        self.label_dealer2.place(x=500, y=80)

        self.label3 = Label(master, text=new_card)
        self.label4 = Label(master, text=new_card2)


        self.label_dealer3 = Label(master, text=dealer_card3)


        # The hit button will give you another card value
        self.hit_button = Button(master, text="Hit", command=self.hit)  # The Button command will create a button.
        self.hit_button.pack()
        self.hit_button.config( height = 2, width = 10, background = "black", foreground = "white")  # Cof=nfig changes how the thing looks
        self.hit_button.place(x=60, y=540) # Will place it in these coords

        # This is the "stand button" that will cause the user to stand, and for them to win, or lose
        self.stand_button = Button(master, text="Stand", command=self.stand)
        self.stand_button.pack()   # This will place the button on the screen
        self.stand_button.config( height = 2, width = 10, background = "black", foreground = "white")
        self.stand_button.place(x=820, y=540)

        if starting_card == 1:
            if starting_card2 == 10:
                print("You got 21! you win!")
            else:
                pass
        else:
            pass

        if starting_card2 == 1:
            if starting_card == 10:
                print("You got 21! you win!")
            else:
                pass
        else:
            pass

        if dealer_card == 1:
            if dealer_card2 == 10:
                print("The dealer got 21! you lose.")
                self.label_dealer2 = Label(master, text=dealer_card2)
                self.label_dealer2.pack()
                self.label_dealer2.place(x=500, y=80)

            else:
                pass
        else:
            pass

        if dealer_card2 == 1:
            if dealer_card == 10:
                print("The dealer got 21! you lose.")
                self.label_dealer = Label(master, text=dealer_card)
                self.label_dealer.pack()
                self.label_dealer.place(x=460, y=80)
            else:
                pass
        else:
            pass



    def hit2(self):
        print("You hit!")
        self.label4.pack()
        self.label4.place(x=450, y=480)
        self.label2.place(x=530, y=480)
        self.label.place(x=420, y=480)
        self.label3.place(x=480, y=480)
        if starting_card+starting_card2+new_card+new_card2 > 21:
            print("You busted! You lost.")
        elif starting_card+starting_card2+new_card+new_card2 == 21:
            print("You win! you got 21!")
        else:
            pass

    def hit(self):
        print("You hit!")
        self.label3.pack()
        self.label2.place(x=510, y=480)
        self.label.place(x=480, y=480)
        self.label3.place(x=450, y=480)
        if starting_card+starting_card2+new_card > 21:
            print("You busted! You lost.")
        elif starting_card+starting_card2+new_card == 21:
            print("You win! you got 21!")
        else:
            # The hit button will give you another card value
            self.hit_button = Button(text="Hit", command=self.hit2)  # The Button command will create a button.
            self.hit_button.pack()
            self.hit_button.config(height = 2, width = 10, background = "black", foreground = "white")  # Cof=nfig changes how the thing looks
            self.hit_button.place(x=60, y=540) # Will place it in these coords









    def stand(self):
        self.hit_button.destroy()
        self.stand_button.destroy()
        print("You stand!")
        if dealer_card+dealer_card2 < 17:
            self.label_dealer = Label(text=dealer_card)
            self.label_dealer.pack()
            self.label_dealer.place(x=540, y=80)
            self.label_dealer2 = Label(text="??")
            self.label_dealer2.pack()
            self.label_dealer2.place(x=500, y=80)
            self.label_dealer3 = Label(text=dealer_card3)
            self.label_dealer3.pack()
            self.label_dealer3.place(x=460, y=80)
            self.label_dealer4 = Label(text=dealer_card4)
            self.label_dealer4.pack()
            self.label_dealer4.place(x=420, y=80)
            if dealer_card+dealer_card2+dealer_card3 < 17:
                time.sleep(0.5)
                self.label_dealer = Label(text=dealer_card)
                self.label_dealer.pack()
                self.label_dealer.place(x=500, y=80)
                self.label_dealer2 = Label(text="??")
                self.label_dealer2.pack()
                self.label_dealer2.place(x=460, y=80)
                self.label_dealer3 = Label(text=dealer_card3)
                self.label_dealer3.pack()
                self.label_dealer3.place(x=420, y=80)
                if dealer_card+dealer_card2+dealer_card3+dealer_card4 < 17:
                    self.label_dealer = Label(text=dealer_card)
                    self.label_dealer.pack()
                    self.label_dealer.place(x=540, y=80)
                    self.label_dealer2 = Label(text="??")
                    self.label_dealer2.pack()
                    self.label_dealer2.place(x=500, y=80)
                    self.label_dealer3 = Label(text=dealer_card3)
                    self.label_dealer3.pack()
                    self.label_dealer3.place(x=460, y=80)
                    self.label_dealer4 = Label(text=dealer_card4)
                    self.label_dealer4.pack()
                    self.label_dealer4.place(x=420, y=80)
            elif dealer_card+dealer_card2+dealer_card3 == 21:
                tims.sleep(0.5)
                print("The dealer got 21! You lose")
            else:
                self.label_dealer2.destroy()
                time.sleep(0.5)
                self.label_dealer2 = Label(text=dealer_card2)
                print("The dealer busted! You win!")
        else:
            print("wiat")



root = Tk()
my_gui = MyFirstGUI(root)
root.geometry("960x640")
root.configure(bg="#00AB4F")
root.mainloop()
