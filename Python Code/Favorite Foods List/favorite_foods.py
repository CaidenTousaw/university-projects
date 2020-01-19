import  #allows time.sleep
import sys
print("At any time, type, 'stop' to stop adding to your list, and type 'list' to show your current list")

favorite_foods = [] #creating an empty array that will be filled with favorite foods

def main(): #the program that does stuff
    global var
    var = input("What is your favorite food?: ")
    if var == "stop": #if the user types stop, the program will not accept any more requests
        print("stopping... ")
        time.sleep(1)
        print("Your final list of favorite foods is: ")
        time.sleep(0.1)
        print(favorite_foods)
        sys.exit(0)
    elif var == "list": #if the user types list, it will print the foods, then allow the user to continue inputting foods
        print(favorite_foods)
        time.sleep(0.25)
        pass
    if var != "list":   #if the thing that was typed is not list, it will add the user input
        favorite_foods.append(var)
    else:
        pass    #the reason i needed (if var !=) is because the list produced would inclide if the user typed 'list'
    time.sleep(0.2)

time.sleep(0.1)
while True:   #will loop as many times until someone types stop
    main()
