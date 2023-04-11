name=input("Enter youre name: ")
choice=input("Do you want to play with me? yes/no ")
from random import randint
loop=0
x=randint(1,11)
if choice.lower()=="yes":
    print(f"Ok {name} lets start the game.\nI choice a number between 1 and 10 ")
    while loop<1000:
        num=int(input("Enter the number: "))
        loop+=1
        if num<x:
            print("youre number less then my!")
        elif num>x:
            print("youre number larger then my!")
        elif num==x:
            print(f"Wow you guess mu number {x} for {loop} attempts")
            break
elif choice.lower()=="no":
    print("I don't want to play with you too (>_<)")
else:
    raise ValueError
    