import random
import time as t


#other things

room = 10
choice = "PLACEHOLDER"
skipintro = input("skip intro? y/n")

#intro
if skipintro == 'n':

	print("welcome to BurgerQuest")
	t.sleep(0.9)
	print("Our main character is Stephen H. Burgerguy, a burger shop owner and chef.")
	t.sleep(1)
	print("Stephen was a normal guy, flipping burgers and cooking burgers and eating burgers")
	t.sleep(1)
	print("Until one day, that all changed.")
	t.sleep(0.9)
	print("A jerkhole customer decided to complain about Stephens flawless burgers!!!")
	t.sleep(1)
	print('"There is no sauce on my burger!!!" the Karen blabbed, completely oblivius to the fact that you put th	sauce on the burger yourself.')
	print("(what an idiot, am i right?)")
	t.sleep(1.5)
	print("After this incident, annoying customers started showing up week after week,")
	t.sleep(1)
	print("day by day,")
	t.sleep(0.9)
	print("hour by hour,")
	t.sleep(0.9)
	print("minute by minute.")
	t.sleep(0.9)
	print("Burgerguy grew tired of these annoying customers.")
	t.sleep(1)
	print("Stephen did some research (on twitter), and it turned out that he had been cursed by the evil BurgerKing,	who resides within a burger dungeon!")
	t.sleep(1.2)
	print("The Burger King was mad that Stephen's burgers were better than his (what a jerk).")
	t.sleep(1.1)
	print("So, Stephen, with his trusty sword (that he bought off craigslist), enters the dungeon to take theBurger		King on")
	t.sleep(1.3)
	print("So begins, BurgerQuest")
	t.sleep(1.5)

#character stats
#item variables

#intentory = ["torch","sword","armor","nothing","nothing"]
inventory = ["torch","sword","armor","shield","potion"]
#              0        1       2       3         4

statnames = ["Health","Average Damage","Armor"]
#MAKE IT SO ARMOR DECREASES AND CANNOT BE REGENERATED, also armor can overflow so if player has 1 armor left and takes a 100 damage hit they still take no damage

stats = [100, 7, 50]
#when you get the sword make average damage stats[1] 15

bossnames = ["north","south","east","west"]
defending = False


#boss fight
#https://gamedev.stackexchange.com/questions/128024/how-can-i-make-text-based-combat-more-engaging
def boss_fight(player_hp, boss_hp, boss_attack, boss_number,player_armor):
	while player_hp > 0 and boss_hp > 0:
		# Player turn ADD DIFFERENT PRINTS and CHOICES DEPENDING ONINVENTORY!!!!!!!!!!!!
		if inventory[4] == "potion":
			if inventory[3] == "shield":
				print("Enter 'attack' to attack, 'defend' to defend, 'potion'to use a potion, or 'talk' to talk: ")
				choices = "attack, defend, potion, talk, help,choices"
			if inventory[3] != "shield":
				print("Enter 'attack' to attack, 'potion' to use potion, or 'talk' to talk: ")
				choices = "attack, potion, talk, help, choices"
		if inventory[4] != "potion":
			if inventory[3] == "shield":
				print("Enter 'attack' to attack, 'defend' to defend, or 'talk' to talk: ")
				choices = "attack, defend, talk, help,choices"
			if inventory[3] != "shield":
				print("Enter 'attack' to attack, or 'talk' to talk: ")
				choices = "attack, talk, help, choices"
		action = input("")
		if action == 'a' or action == 'attack':
			# Player attacks
			if inventory[1] == "sword":
			#roll the dice when ever the player chooses attack.
				damage_calc = random.randint(5,8)
				if damage_calc == 8:
					player_attack = 10
					print("Critical Hit! 10 Damage!")
				else:
					player_attack = damage_calc
			if inventory[1] == "cleaver":
				damage_calc = random.randint(10,14)
				if damage_calc == 14:
					player_attack = 20
					print("CRITICAL HIT! 10 DAMAGE!")
				else:
					player_attack = damage_calc
			boss_hp -= player_attack
			print(f"You hit {bossnames[boss_number]} for {player_attack}damage!")
		if action == 'd' or action == 'defend':
			# Player defends
			print(f"You brace for {bossnames[boss_number]}'s attack.")
		elif action == 't' or action == 'defend':
			# Player attempts to talk
			success = random.random() < 0.15
			if success:
				print("You successfully talked your way out of th fight!")
				break
			else:
				print("Your attempt to talk failed.")
		elif action == 'h' or action == 'help':
			print(f"inventory{inventory}")
			for i in range(3):
				print(f"{statnames[i]}:{stat[i]}")
		elif action == 'c' or action == 'choices':
			print(choices)
		# Boss attacks
		if boss_hp > 0:
			if action == 'd':
				# Player takes reduced damage when defending
				if player_armor > 0:
					player_armor -= int(boss_attack /2)
					print(f"{bossnames[boss_number]}hits you for{int (boss_attack / 2)} damage! Your armor takes the hit!")
				else:
					player_hp -= int(boss_attack / 2)
					print(f"{bossnames[boss_number]}hits you for{int (boss_attack / 2)} damage!")
				stats[0] = player_hp
				stats[2] = player_armor
			else:
				if player_armor > 0:
					player_armor -= boss_attack
					print(f"{bossnames[boss_number]}hits you for {boss_attack} damage Your armor	takes the hit!")
				else:
					player_hp -= boss_attack
					print(f"{bossnames[boss_number]}hits you for {boss_attack} damage!")
				stats[0] = player_hp
				stats[2] = player_armor
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


def bigbooty():
	if choice == 'help' or choice == 'h':
		help()
	if choice == 'choices' or choice == 'c':
		print(choices)

skiptutorial = input("skip tutorial? y/n")
if skiptutorial == 'n':
	print('')
	print('')
	print('')
	print("IMPORTANT tutorial PLEASE READ:")
	print("when entering your options, you can either enter the full choice or just the first letter")
	print("you can type help at any time to view your inventory and stats")
	print("you can also type choices at any time to view your choices")
while True:
	if room == 10:
		choices = "north, south, east, west, help, choices"
		print("You are in a grand hall. There are four doors to north, east, south, and westrespectively.")
		choice = input("")
		bigbooty()
		if choice == 'break' or choice == 'quit':
			break
		if choice == 'north' or choice == 'n':
			room = 20
	if room == 20:
		print("You are in a dark, damp hallway. There are two doors. One lies to the north, and the otherto the	east")
		choice = input("You can also go back to the previous room.")
	if stats[0] <= 0:
		break
print("")
print("No, you’re NOT a real gamer.")
print("")
print("I’m so sick of all these people that think they’re gamers. No, you’re not. Most of you are not even close to being gamers.I see these people saying “I put well over 100 hours in this game, it’s great!” that’s nothing, most of us can easily put 300+ hours in all our games.I see people who only have a Nintendo Switch and claim to be gamers. Come talk to me when you pick up a PS4 controller then we be friends.")
print("Also DEAR ALL WOMEN: Pokémon is not a real game. Animal Crossing is not a real game. The Sims is not a real game. Mario is not a real game. Stardew valley is not a real game. Mobile games are NOT.REAL.GAMES. put down the baby games and play something that requires challenge and skill for once.")
print("")
print("Sincerely, all of the ACTUAL gamers.")