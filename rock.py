#!/usr/bin/env python3

from colors import red, green, blue

print(red('This is red'))
print(green('This is green'))
print(blue('This is blue'))


user1 = input("What is your name? ")
user2 = input("What is your name? ")
user1_input = input("Hello %s, what is your choice? Rock, Scissors or Paper? " % user1).lower()
user2_input = input("Hello %s, what is your choice? Rock, Scissors or Paper? " % user2).lower()
inputs = user1_input, user2_input

def compare(u1, u2):
    if u1 == u2:
        return("It is tie. One more round")
    elif u1 == "rock":
        if u2 == "scissors":
            return(f"{user1} wins!!!")
        else:
            return(f"{user2} wins!!!")
    elif u1 == "scissors":
        if u2 == "paper":
            return(f"{user1} wins!!!")
        else:
            return(f"{user2} wins!!!")
    elif u1 == "paper":
        if u2 == "rock":
            return(f"{user1} wins!!!")
        else:
            return(f"{user2} wins!!!")
    else:
        return("Invalid input")


print(compare(user1_input, user2_input))
