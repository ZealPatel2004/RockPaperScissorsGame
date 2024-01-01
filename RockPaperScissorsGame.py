#This is a game of Rock, papers and scissors
import random

choices=["rock","paper","scissors"]
computer=random.choice(choices)#This will get for computer a random value.

player=None
while player not in choices:
    player=input("rock,paper or scissors: ").lower()#This will make capital case letters lower case

if player==computer:
    print("computer chose: "+computer)
    print("Player chose: "+player)
    print("This is a tie")
elif player=="rock":
    if computer=="paper":
        print("computer chose: "+computer)
        print("Player chose: "+player)
        print("you lose")
    if computer=="scissors":
        print("computer chose: "+computer)
        print("Player chose: "+player)
        print("you win")
elif player=="scissors":
    if computer=="rock":
        print("computer chose: "+computer)
        print("Player chose: "+player)
        print("you lose")
    if computer=="paper":
        print("computer chose: " + computer)
        print("Player chose: " + player)
        print("you win")
elif player=="paper":
    if computer=="scissors":
        print("computer chose: " + computer)
        print("Player chose: " + player)
        print("you lose")
    if computer=="rock":
        print("computer chose: " + computer)
        print("Player chose: " + player)
        print("you win")








