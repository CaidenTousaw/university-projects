import math
# this program will convert your units to any other unit you would
# like in the same category. coded by: Caiden Tousaw

ans = 0 #defining the variable as a blank so i can change it later in the code

def another():
    another = str(input("Would you like to perform another conversion?: "))
    if another == "yes":
        initial()
    else:
        print("okay, you can close the program now")

def length():
   if unit1 == "mm" and unit2 == "cm": #if the user typed mm first and cm second, the answer will change from 0 to (your value) times 10
       ans = num/10
       print("the answer of your conversion is", ans) #if the user typed mm first and cm second, the answer will change from 0 to (your value) divided by 10
       another()
   elif unit1 == "cm" and unit2 == "mm":              #this changed because the convertion math is different, you will see the math part change because of the conversion rates
       ans = num*10
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "mm" and unit2 == "inch":
       ans = num/25.4
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "inch" and unit2 == "mm":
       ans = num*25.4
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "cm" and unit2 == "inch":
       ans = num/2.54
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "inch" and unit2 == "cm":
       ans = num*2.54
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "mm" and unit2 == "foot":
       ans = num/205
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "foot" and unit2 == "mm":
       ans = num*205
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "cm" and unit2 == "foot":
       ans = num/30.48
       print("the answer of your conversion is", ans)
       another()
   elif unit1 == "foot" and unit2 == "cm":
       ans = num*30.48
       print("the answer of your conversion is", ans)
       another()
   else:
        print("this conversion is not available, sorry.") #if users tey to say anything above days, it will give this error because the conversion if too high
        another()

def weight():
    if unit1 == "lbs" and unit2 == "kg": #because there are only two options for this conversion, i dont need an elif, i can use the else statement for this instead
        ans = num/2.205
        print("the answer of your conversion is", ans)
        another()
    else:
        ans = num*2.205
        print("the answer of your conversion is", ans)
        another()


def time(): #same conversions as length with different math, not going to comment on this part of the code anymore because it is self-explanitory.
    if unit1 == "seconds" and unit2 == "minutes":
        ans = num/60
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "minutes" and unit2 == "seconds":
        ans = num*60
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "seconds" and unit2 == "hours":
        ans = num/3600
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "hours" and unit2 == "seconds":
        ans = num*3600
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "minutes" and unit2 == "hours":
        ans = num/60
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "hours" and unit2 == "minutes":
        ans = num*60
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "seconds" and unit2 == "days":
        ans = num/86400
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "days" and unit2 == "seconds":
        ans = num*86400
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "minutes" and unit2 == "days":
        ans = num/1440
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "days" and unit2 == "minutes":
        ans = num*1440
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "hours" and unit2 == "days":
        ans = num/24
        print("the answer of your conversion is", ans)
        another()
    elif unit1 == "days" and unit2 == "hours":
        ans = num*24
        print("the answer of your conversion is", ans)
        another()
    else:
        print("this program does not support that conversion, sorry.")
        another() #runs ther code that asks for another go

def temp():
    if unit1 == "f" and unit2 == "c":
        ans = num-32
        ans = ans*5/9
        print("the answer of your conversion is", ans)
        another()
    else:
        ans = num*9/5
        ans = ans + 32
        print("the answer of your conversion is", ans)
        another() #runs ther code that asks for another go

def initial():
    global question
    global unit1
    global unit2
    global num
    print("Welcome to my unit converter, we support length, weight, time and temperature conversions") #introduction to the program, tells the user what it does.
    question = str(input("What unit type would you like to convert?: "))
    if question == "length":
        unit1 = str(input("What would you like to convert from? (cm, mm, inch, foot): "))        #storing these for later when the program needs to choose what if statement to act on
        unit2 = str(input("What would you like to convert to? (cm, mm, inch, foot): "))
        num = float(input("What is the value?: "))
    elif question == "weight":
                unit1 = str(input("What would you like to convert from? (lbs & kg): "))        #storing these for later when the program needs to choose what if statement to act on
                unit2 = str(input("What would you like to convert to? (lbs & kg): "))
                num = float(input("What is the value?: "))
    elif question == "time":
                unit1 = str(input("What would you like to convert from? (seconds, minutes, hours, and days): "))        #storing these for later when the program needs to choose what if statement to act on
                unit2 = str(input("What would you like to convert to? (seconds, minutes, hours, and days): "))
                num = float(input("What is the value?: "))
    elif question == temp:
        unit1 = str(input("What would you like to convert from? (f and c): "))        #storing these for later when the program needs to choose what if statement to act on
        unit2 = str(input("What would you like to convert to? (f and c): "))
        num = float(input("What is the value?: "))
    else:
        print("this conversion is not supported, sorry!")
        another()


def main():

    if question == "length":
        length()

    elif question == "weight":         #basic program that actually does the stuff
        weight()

    elif question == "time":
      time()

    else:
      temp()

initial()
main() #run it
