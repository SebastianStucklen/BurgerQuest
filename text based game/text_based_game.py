import random
import time
room = 1
choice = "PLACEHOLDER"
test = 1
print("welcome to")
time.sleep(1)
print("cool")
time.sleep(0.8)
print("dungeon")
time.sleep(0.8)
print("GUY")
time.sleep(2)
print("the greatest game since mort the chicken on the ps2")
time.sleep(1)
print("Type help for help")
inventory = []
hasShield = False
sword = 7 #change this to 15 when player gets upgraded sword
hasPotion = False
def bossFight(name,health,attack):
    #put stuff here later
    print("placeholder")
def help():
    #put stuff here
    print("Type I to view inventory")
while choice != "quit":
    if room == 1:
        choice = input("You are in a grand hall. There are four doors. north, east, south, and west.")
        if choice == 'help':
            help()