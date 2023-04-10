import random
import time as t
def pause():
    programPause = input("Press the <ENTER> key to continue...")

#other things

room = 10
choice = "PLACEHOLDER"

#character stats
#item variables

intentory = ["torch","sword","armor","nothing","burger"]
#inventory = ["torch","sword","armor","shield","burger"]
#              0        1       2       3         4

statnames = ["Health","Average Damage","Armor"]
#MAKE IT SO ARMOR DECREASES AND CANNOT BE REGENERATED, also armor can overflow so if player has 1 armor left and takes a 100 damage hit they still take no damage
attackTypes = ["sweep","stab","slice","bash"]
stats = [100, 7, 50]
burger = 100

#each burger heals 100
#when you get the sword make average damage stats[1] 15

bossnames = ["north","south","east","west","Zomburger"]
#monster types
#zomburger: 80 hp, 10 damage, 4, 0
defending = False


#boss fight
#https://gamedev.stackexchange.com/questions/128024/how-can-i-make-text-based-combat-more-engaging
def boss_fight(player_hp, player_armor, boss_hp, boss_attack, boss_number, boss_defense):
	print("I havent coded potions/burgers yet so it wont work")
	choices = ["attack", "defend", "burger", "talk", "help","choices"]
	turnOver = False
	hasTalked = False
	dismembered = False
	stabbed = 0
	stunned = 0
	bleeding = 0
	while player_hp > 0 and boss_hp > 0:
		if stabbed <= 0:
			while turnOver == False:
				# Player turn ADD DIFFERENT PRINTS and CHOICES DEPENDING ONINVENTORY!!!!!!!!!!!!
				# make it so character can do multiple attacks with varying damage
				# but boss has a chance to dodge these attacks
				# code burger
				# make it so player can pick how much of the burger they want to use
				if inventory[4] == "burger":
					if inventory[3] == "shield":
						print("Enter 'attack' to attack, 'defend' to defend, 'burger'to use a burger, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
					if inventory[3] != "shield":
						print("Enter 'attack' to attack, 'burger' to use burger, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
						choices[1] = "nothing"
				if inventory[4] != "burger":
					choices[2] = "nothing"
					if inventory[3] == "shield":
						print("Enter 'attack' to attack, 'defend' to defend, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
					if inventory[3] != "shield":
						print("Enter 'attack' to attack, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
						choices[1] = "nothing"

				action = input("")
				print("")


				if action == 'a' or action == 'attack':
					#attackTypes = ["sweep","stab","slice","bash"]
					sweep = stats[1] + 10
					stab = stats[1] + 5
					slice = stats[1]
					bash = 3
					#boss cant dodge if stunned
					#Player attacks
					#roll the dice when ever the player chooses attack.
					#attack types
					#Big Sweep: High damage, high chance to be dodged, can cause bleeding on crit (instead of extra)
					#Stab: High damage, Causes bleeding, cant be dodged, player misses their next turn
					#Quick Slice: Average Damage, low chance to be dodged.
					#Shield Bash: Low Damage, stuns boss (miss their next turn)
					#High dodge chance = 80
					#average dodge chance = 40
					#low dodge chance = 20
					print("Attack Types:")
					print("Big Sweep: An incredibly high damage and bloodletting attack with a somewhat high chance for the boss to dodge. Has a chance to cause dismemberment.")
					print("Stab: A high damage and bloodletting attack which can't be dodged. However, you have a chance to miss your next turn.")
					print("Quick Slice: An average attack with average damage. Low chance to be dodged.")
					print("Shield Bash: A low damage attack that causes the boss to lose their turn. Average chance to be dodged.")
					print("Which attack would you like to do?")
					attackChoice = input("Type: sweep, stab, slice, or bash.")
					if choice == "sweep":
						dodge = random.randint(0,100)
						if dodge > 80: 
							damage_calc = random.randint(sweep-3,sweep+3)
							if damage_calc == sweep+3:
								player_attack = sweep+2
								print("Critical Hit!")
								dismemberChance = random.random() < 0.7
								if dismemberChance:
									dismembered = True
							elif damage_calc == sweep-3:
								player_attack = sweep-3
								print("Crappy Hit!")
							else:
								player_attack = damage_calc
							boss_hp -= player_attack
							print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
						elif dodge <= 80:
							print(f"{bossnames[boss_number]} dodged your attack!")
						turnOver = True


				if action == 'd' or action == 'defend':
					# Player defends
					print(f"You brace for {bossnames[boss_number]}'s attack.")
					turnOver = True


				elif action == 't' or action == 'talk':
					if hasTalked == False:
						# Player attempts to talk
						success = random.random() < 0.15
						if success:
							if success <= 0.33:
								print(f"You managed to convince {bossnames[boss_number]} thats they're fighting for an unjust cause.")
							elif success <= 0.66:
								print(f"You give {bossnames[boss_number]} a bite of one of your your. They love it!")
							elif success <= 1:
								print(f"You beat {bossnames[boss_number]} in a game of rock-paper-scissors. They are legaly required to give up.")
							else:
								print("You successfully talked your way out of a fight. Nice.")
							break
						else:
							print(f"Your attempt to talk failed. Now {bossnames[boss_number]} really hates you.")
							turnOver = True
						hasTalked = True
					else:
						print(f"{bossnames[boss_number]} already hates you. Try something else.")


				elif action == 'h' or action == 'help':
					print(f"inventory{inventory}")
					for i in range(3):
						print(f"{statnames[i]}:{stats[i]}")

				elif action == 'c' or action == 'choices':
					print(choices)
				
		else:
			print("You retrieve your sword, but you miss your attack as a result.")
		print("")

		# Boss attacks
		if dismembered == True:
			boss_attack-=(boss_attack/3)
		if stunned <= 0:
			if action == 'd':
				# Player takes reduced damage when defending
				if player_armor > 0:
					player_armor -= int(boss_attack /2)
					print(f"{bossnames[boss_number]} hits you for{int (boss_attack / 2)} damage! Your armor takes the hit!")
				else:
					player_hp -= int(boss_attack / 2)
					print(f"{bossnames[boss_number]} hits you for{int (boss_attack / 2)} damage!")


			else:
				if player_armor > 0:
					player_armor -= boss_attack
					print(f"{bossnames[boss_number]} hits you for {boss_attack} damage. Your armor takes the hit!")
				else:
					player_hp -= boss_attack
					print(f"{bossnames[boss_number]} hits you for {boss_attack} damage!")
		else:
			print(f"{bossnames[boss_number]} is still stunned!")
		stats[0] = player_hp
		stats[2] = player_armor
		turnOver = False
		if stabbed > 0:
			stabbed-=1
		if stunned > 0:
			stunned-=1
		if bleeding > 0:
			bleeding-=1
		print("")
		print(f"Your HP: {player_hp}")
		print(f"Boss HP: {boss_hp}")
		pause()
	if player_hp <= 0:
		stats[0] = 0
		print(f"You have been defeated by {bossnames[boss_number]}.")
	elif boss_hp <= 0:
		bossnames[boss_number] = "dead"
		print(f"You have defeated {bossnames[boss_number]}!")
		print("Your burger has been refilled!")
		#REFILL POTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#boss_fight(stats[0], stats[2], 100, 20, 1, 0)
#help

skipintro = input("skip intro? y/n")

#intro
if skipintro == 'n':
	print('')
	print("welcome to BurgerQuest")
	print('')
	pause()
	print("Our main character is Stephen H. Burgerguy, a burger shop owner and chef.")
	print('')
	pause()
	print("Stephen was a normal guy, flipping burgers and cooking burgers and eating burgers")
	print('')
	pause()
	print("Until one day, that all changed.")
	print('')
	pause()
	print("A jerkhole customer decided to complain about Stephens flawless burgers!!!")
	print('')
	pause()
	print('"There is no sauce on my burger!!!" the Karen blabbed, completely oblivius to the fact that you put th	sauce on the burger yourself.')
	print("(what an idiot, am i right?)")
	print('')
	pause()
	print("After this incident, annoying customers started showing up week after week,")
	print('')
	pause()
	print("day by day,")
	print('')
	pause()
	print("hour by hour,")
	print('')
	pause()
	print("minute by minute.")
	print('')
	pause()
	print("Burgerguy grew tired of these annoying customers.")
	print('')
	pause()
	print("Stephen did some research (on twitter), and it turned out that he had been cursed by the evil BurgerKing,	who resides within a burger dungeon!")
	print('')
	pause()
	print("The Burger King was mad that Stephen's burgers were better than his (what a jerk).")
	print('')
	pause()
	print("So, Stephen, with his trusty sword (that he bought off craigslist), enters the dungeon to take the Burger King on")
	print('')
	pause()
	print("So begins, BurgerQuest")
	print('')
	pause()


skiptutorial = input("skip tutorial? y/n")

if skiptutorial == 'n':
	print('')
	print('')
	print('')
	print("IMPORTANT tutorial PLEASE READ:")
	print("when entering your options, you can either enter the full choice or just the first letter")
	print("you can type help at any time to view your inventory and stats")
	print("you can also type choices at any time to view your choices")

#this is for the random monster encounters
monsterRooms = ["false","false","false","false"]
#1,5,9 is room 20
#2,6,10 is room 30
#3,7,11 is room 40
#4,8,12 is room 50
#maybe code multiple monster fights eventually
for i in range(4):
	placeholder = random.randint(1,5)
	#print(placeholder)
	##room 20
	if placeholder == 1:
		monsterRooms[0] = "true"
	#if placeholder == 5:
	#	monsterRooms[0] = "double"
	#if placeholder == 9:
	#	monsterRooms[0] = "triple"
	##room 30
	if placeholder == 2:
		monsterRooms[1] = "true"
	#if placeholder == 6:
	#	monsterRooms[1] = "double"
	#if placeholder == 10:
	#	monsterRooms[1] = "triple"
	##room 40
	if placeholder == 3:
		monsterRooms[2] = "true"
	#if placeholder == 7:
	#	monsterRooms[2] = "double"
	#if placeholder == 11:
	#	monsterRooms[2] = "triple"
	##room 50
	if placeholder == 4:
		monsterRooms[3] = "true"
	#if placeholder == 8:
	#	monsterRooms[3] = "double"
	#if placeholder == 12:
	#	monsterRooms[3] = "triple"
def help():
	print(f"inventory{inventory}")
	for i in range(3):
		print(f"{statnames[i]}:{stats[i]}")


def bigbooty():
	if choice == 'help' or choice == 'h':
		help()
	if choice == 'choices' or choice == 'c':
		print(choices)
	if choice == 'mon':
		print(monsterRooms)

for i in range(10):
	testerre = random.randint(5-3,5+3)
	print(testerre)
while True:
	if room == 10:
		choices = "north, south, east, west, help, choices"
		print("You are in a grand hall.")
		print(" There are four doors to north, east, south, and west respectively.")
		choice = input("")
		bigbooty()
		if choice == 'break' or choice == 'quit':
			break
		if choice == 'north' or choice == 'n':
			room = 20

	if room == 20:
		if monsterRooms[0] == "true":
			print("a thaiuyadw attacks")
			boss_fight(stats[0], stats[2], 80, 10, 4, 0)
		print("You are in a dark, damp hallway.")
		choice = input("")
		bigbooty()
		if choice == 'break' or choice == 'quit':
			break
	if stats[0] <= 0:
		break
print("")
print("No, you’re NOT a real gamer.")
print("")
print("I’m so sick of all these people that think they’re gamers. No, you’re not. Most of you are not even close to being gamers.I see these people saying “I put well over 100 hours in this game, it’s great!” that’s nothing, most of us can easily put 300+ hours in all our games.I see people who only have a Nintendo Switch and claim to be gamers. Come talk to me when you pick up a PS4 controller then we be friends.")
print("Also DEAR ALL WOMEN: Pokémon is not a real game. Animal Crossing is not a real game. The Sims is not a real game. Mario is not a real game. Stardew valley is not a real game. Mobile games are NOT.REAL.GAMES. put down the baby games and play something that requires challenge and skill for once.")
print("")
print("Sincerely, all of the ACTUAL gamers.")