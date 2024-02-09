#!/usr/bin/env python3


def main():

    print("You've come to play rock paper scissors I see")
    print("let's see who will win today")

#users
user1 = input("Make your choice")
user2 = input("make your choice")

if (user1 == "scissors" and user2 == "rock"):
    print("user2 winner!")

elif (user1 == "scissors" and user2 == "paper"):
    print("user1 winner!")

elif (user1 == "scissors" and user2 == "scissors"):          
    print("We have a tie!")

elif (user1 == "rock" and user2 == "paper"):    
    print("user1 winner!")

elif (user1 == "rock" and user2 == "scissors"):    
    print("user1 winner!")    

elif (user1 == "rock" and user2 == "rock"): 
    print("We have a tie!")

elif (user1 == "paper" and user2 == "rock"):
    print("user2 winner!")

elif (user1 == "paper" and user2 == "scissors"):   
    print("user2 winner!")

elif (user1 == "paper" and user2 == "paper"):  
    print("We have a tie!") 

else: 
    ("Make the right selection brahhh, there's only 3 choices")

#end of game note
    print("If you lost try to read their mind better")


main()
