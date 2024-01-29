##+-----------------------------------------------------------------------
##
## Python Game - (c) 2024 Chris Londal.  All Rights Reserved.
##
## File:        Game.py
##
## Description:
##
##   A game that I wanted to create in python. It is meant to have an economy.
##  
##
## History:     Jan-24-2024     cfl429bc      Created
##
##------------------------------------------------------------------------

## Game step setup
step = int(1)
#money = int(input("Amount of starting money: "))
money = int(100)
inventory = ["empty", "empty", "empty", "empty", "empty"]
inventory[1] = str("Dog")
inventory[2] = str("Cat")

## Intro to my game
if step == 1:
    #player_name = str(input("Lets get to know you. \nWhat is your name? \nType it here:"))
    player_name = ("Chris")
    msg = print(f"Hello {player_name} I am a text based game made by -REDACTED-!")

while step < 5:
    print(f"You have ${money}")
    print(f"Inventory: \nSlot 1: {inventory[0]} \nSlot 2: {inventory[1]} \nSlot 3: {inventory[2]} \nSlot 4: {inventory[3]} \nSlot 5: {inventory[4]}")
    action = str(input("Buy or Sell: "))

    if action == ("buy"):
        if money == 0:
            print("You're damn broke")
            if inventory[0] == ("empty"):
                if inventory[1] == ("empty"):
                    if inventory[2] == ("empty"):
                        if inventory[3] == ("empty"):
                            if inventory[4] == ("empty"):
                                print("You have nothing to sell either. \nNow you're dead")
                                break
            
            print("Sell something you dimwit")
            action = str("sell")
            continue
       
        item = str(input("What are you buying? "))
        transaction = int(input("How much are you paying: "))
        slot_num = int(input("Which slot are you storing it in? 1 through 5: "))
        slot = (slot_num - 1)
        inventory[slot] = str(f"{item}")
        money = (money - transaction)
        
        if money < 0:
            debt = (money * (-1))
            print(f"You owe ${debt} so you need to sell something or go to jail.")
            action = str("sell")

    
    
    if action == ("sell"):
        slot_num = int(input("Which slot would you like to sell? 1 through 5: "))
        slot = (slot_num - 1)
        
        if inventory[slot] == ("empty"):
            print("You can't scam people. \nNow you're dead")
            break
        
        transaction = int(input(f"How much would you like to sell your {inventory[slot]} for? "))
        inventory[slot] = str("empty")
        money = (money + transaction)
    
    print(f"Step {step}")
    step = step + 1

    
