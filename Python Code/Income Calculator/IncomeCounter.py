import time

minutes = ["mins", "minutes", "Mins", "Minutes", "m", "M", "Mins", "mins"]
seconds = ["seconds", "secs", "s", "Seconds", "Secs", "S"]     #Arrays that hold all the ways someone could type "minute", or "second"


income = int(input("How much money do you make an hour?: "))

minutePay = income/60    #60 mins in an hour, so dividing hourly pay by 60 will give you minute pay

secondPay = minutePay/60   #60 seconds a minute, dividing minute pay by 60 will give you second pay

totalTime = 0

def minuteIncome():     # Will print your minute-ly income, once a minute
    while True:
        global totalTime
        totalTime = totalTime + 1   # just adds a new 'tick' if you could call it, to the counter.
        time.sleep(30)
        print(minutePay*totalTime) # this will print the minutepay * 'tick' count. every minute
        time.sleep(30)


def secondIncome():
    while True:
        global totalTime
        totalTime = totalTime + 1 # again this is the 'tick' count
        time.sleep(0.5)
        print(secondPay*totalTime) # because the tick count goes up by one a second, it will print the secondpay every second.
        time.sleep(0.5)



def main():
     minuteOrSecond = str(input("Would you like to see your pay increase by minutes, or seconds?: "))
     if minuteOrSecond in minutes:  # checks if the input was in the array with the answers in it. LINE 3
         minuteIncome()

     elif minuteOrSecond in seconds: # checks if the input was in the array with the answers in it. LINE 4
         secondIncome()
     else:
        print("That's not an option!") #if the user types anything else, it will restart the main() function.
        time.sleep(0.5)
        main()

main()  #runs the program
