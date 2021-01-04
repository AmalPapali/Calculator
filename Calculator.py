# ok so this works :)
# we are defining our own variables
# to tell the program what to do when we call these
# now we just need to gather all our previous code
# so the program works but when we exit from something it exits us from everything
# so lets do this
def main():
    print ("This is a calculator made with Python")
    print ("Created by Amal Papali")
    print ("A is Add, S is Subtract, M is Multiply, D is Divide")
    choose = input ("Which option?")
    if choose.lower() == "a":
        add()
    elif choose.lower() == "s":
        subtract()
    elif choose.lower() == "m":
        multiply()
    elif choose.lower() == "d":
        divide()
    elif choose.lower() == "exit":
        exit()
    else:
        print ("I didn't understand your response")
def subtract():
    while True:
        #This program has to ask the user for the first integer
        num1 = input("What is your first integer? ")
        if num1 == "exit":
            main()
        else:
            pass
        #Now it has to ask for the second integer
        num2 = int(input("What is your second integer? "))
        if num2 == "exit":
            main()
        else:
            pass
        total = int(num1) - int(num2)
        print (total)
def multiply():
    while True:
        num1 = input("What is your first number? ")
        if num1.lower() == "exit":
            main()
        #this asks the user for their first number
        num2 = input("What is your second number? ")
        if num2.lower() == "exit":
            main()
        product = int(num1) * int(num2)
        print (product)
def add():
    while True:
        #This program has to ask the user for the first integer
        num1 = input("What is your first integer? ")
        if num1.lower() == "exit":
            main()
        #Now it has to ask for the second integer
        num2 = input("What is your second integer? ")
        if num2.lower() == "exit":
            main()
        total = int(num1) + int(num2)
        print (total)
def divide():
    while True:
        num1 = input("What is your first number? ")
        if num1.lower() == "exit":
            main()
        #this asks the user for their first number
        num2 = input("What is your second number? ")
        if num2.lower() == "exit":
            main()
        product = float(num1) / float(num2)
        print (product)

main()
# YAY IT WORKS :) :) :)
# ill post the code in github for those who want it
# like share and sub
# thx for watching :)
