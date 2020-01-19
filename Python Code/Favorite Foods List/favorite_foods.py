import time
import sys
print("At any time, type, 'stop' to stop adding to your list, and type 'list' to show your current list")

favorite_foods = []

def main():
    global var
    var = input("What is your favorite food?: ")
    if var == "stop":
        print("stopping... ")
        time.sleep(1)
        print("Your final list of favorite foods is: ")
        time.sleep(0.1)
        print(favorite_foods)
        sys.exit(0)
    elif var == "list":
        print(favorite_foods)
        time.sleep(0.25)
        pass
    if var != "list":
        favorite_foods.append(var)
    else:
        pass
    time.sleep(0.2)

time.sleep(0.1)
while True:
    main()