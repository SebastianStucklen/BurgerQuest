import random
import time
#other things
room = 10
choice = "PLACEHOLDER"
#intro
def intro():
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
#intro()
#character stats
#item variables
#intentory = ["torch","sword","armor","nothing","nothing"]
inventory = ["torch","sword","armor","shield","potion"]
statnames = ["Health","Average Damage","Armor"]
#MAKE IT SO ARMOR DECREASES AND CANNOT BE REGENERATED, also armor can overflow so if player has 1 armor left and takes a 100 damage hit they still take no damage
stats = [100, 7, 50]
#when you get the sword make average damage stats[1] 15
bossnames = ["north","south","east","west"]
defending = False
#boss fight
#https://gamedev.stackexchange.com/questions/128024/how-can-i-make-text-based-combat-more-engaging
def boss_fight(player_hp, boss_hp, boss_attack, boss_number):
    if inventory[1] == "sword":
        #roll the dice when ever the player chooses attack.
        player_attack = 7
    if inventory[1] == "cleaver":
        player_attack = 16
    while player_hp > 0 and boss_hp > 0:
        # Player turn ADD DIFFERENT PRINTS and CHOICES   DEPENDING ON INVENTORY!!!!!!!!!!!!
        if inventory[4] != "nothing":
            if inventory[5] != "nothing":
                print("Enter 'attack' to attack, 'defend' to defend, 'potion' to use a potion, or 'talk' to talk: ")
                choices = "attack, defend, potion, talk, help, choices"
            action = input("")
        if inventory[4] == "nothing":
            print("Enter 'attack' to attack, 'defend' to defend, 'potion' to use a potion, or 'talk' to talk: ")
            choices = "attack, defend, talk, help, choices"
            action = input("")
        if action == 'a' or action == 'attack':
            # Player attacks
            boss_hp -= player_attack
            print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
        elif action == 'd' or action == 'defend':
            # Player defends
            print(f"You brace for {bossnames[boss_number]}'s attack.")
        elif action == 't' or action == 'defend':
            # Player attempts to talk
            success = random.random() < 0.15
            if success:
                print("You successfully talked your way out of the fight!")
                break
            else:
                print("Your attempt to talk failed.")
        elif action == 'h' or action == 'help':
                print(f"inventory{inventory}")
                for i in range(3):
                    print(f"{statnames[i]}:{stats[i]}")
        elif action == 'c' or action == 'choices':
            print(choices)
        # Boss attacks
        if boss_hp > 0:
            if action == 'd':
                # Player takes reduced damage when defending
                player_hp -= int(boss_attack / 2)
                print(f"{bossnames[boss_number]} hits you for {int(boss_attack / 2)} damage!")
            else:
                player_hp -= boss_attack
                print(f"{bossnames[boss_number]} hits you for {boss_attack} damage!")
        print(f"Your HP: {player_hp}")
        print(f"Boss HP: {boss_hp}")
    if player_hp <= 0:
        stats[0] = 0
        print(f"You have been defeated by {bossnames[boss_number]}.")
    elif boss_hp <= 0:
        bossnames[boss_number] = "dead"
        print(f"You have defeated {bossnames[boss_number]}!")
#help
def help():
    print(f"inventory{inventory}")
    for i in range(3):
        print(f"{statnames[i]}:{stats[i]}")
print("IMPORTANT tutorial PLEASE READ:")
print("when entering your options, you can either enter the full choice or just the first letter")
print("you can type help at any time to view your inventory and stats")
print("you can also type choices at any time to view your choices")

while True:
    if room == 10:
        choices = "north, south, east, west, help, choices"
        print("You are in a grand hall. There are four doors to north, east, south, and west respectively.")
        choice = input("")
        if choice == 'help' or choice == 'h':
            help()
        if choice == 'choices' or choice == 'c':
            print(choices)
        if choice == 'north' or choice == 'n':
            room = 20
    if room == 20:
        print("You are in a dark, damp hallway. There are two doors. One lies to the north, and the other to the east")
        choice = input("You can also go back to the previous room.")
    if stats[0] <= 0:
        break
print("you dead")