import random
import time as t
def pause():
	programPause = input("Press the <ENTER> key to continue...")
	print("")

#other things

room = 10
choice = "PLACEHOLDER"

#character stats
#item variables

#inventory = ["torch","sword","armor","shield","burger","key piece"]
torchN = 0
swordN = 1
armorN = 2
shieldN = 3
burgerN = 4
keyN = 5
itemNames = ["Grease Torch","Fry Sword","Burger Bun Armor","Pickle Shield","Burger","Key Piece"]
inventory = ["torch","sword","nothing","nothing","burger","nothing"]
#              0        1       2       3         4        5

keypieces = 0
#MAKE BOSS ROOMS
attackTypes = ["sweep","stab","slice","bash"]
#MAKE IT SO ARMOR DECREASES AND CANNOT BE REGENERATED, also armor can overflow so if player has 1 armor left and takes a 100 damage hit they still take no damage

statnames = ["Health","Average Damage","Armor","BurgerBux","Burger%"]
stats = [100, 7 , 0, 0 , 100]
Health = 0
AverageDamage = 1
Armor = 2
BurgerBux = 3
BurgerP = 4
#stats2 = list(stats)
#stats.append("test")
#print(stats)
#stats2.append("test2")
#print(stats2)
#stats = stats2
#stats.append("test3")
#print(stats)
#each burger heals 100
#when you get the sword make average damage stats[1] 15
def healthRand(a,b):
	eichpee = random.randint(a,b)
	return eichpee
bossnames = ["Phil W. Frencherfrie","Patty Clown Kidnapper","Mouse with Sewing Needle","Evil Cup of Water","Zomburger","Cheese Cat-Slime"]
zomburger = [healthRand(70,90), 10, 4]
slime = [healthRand(30,50),20,5]
#bosses
patty = [200,15,1]
rat = [300,5,2]

#monster types
#zomburger: 80 hp, 10 average damage, number: 4
phil = []
def help():
	print(f"inventory: {inventory}")
	
	varkle = len(statnames)
	varble = len(stats)
	for i in range(varkle):
		print(f"{statnames[i]}: {stats[i]}")

def search_item(list, item):
	for i in range(len(list)):
		if list[i] == item:
			return True
	return False

#BATTLE SYSTEM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def boss_fight(boss_hp, boss_attack, boss_number):
	player_hp = stats[Health]
	player_armor = stats[Armor]
	burgerPercent = stats[BurgerP]
	bossDamage = boss_attack
	choices = ["attack", "defend", "burger", "talk", "help","choices"]
	turnOver = False
	viewedAttacks = False
	hasTalked = False
	talkSucc = False
	dismembered = False
	defending = False
	attackCharging = False
	stabbed = 0
	stunned = 0
	bossBleeding = 0
	playerPoisoned = 0
	
	print(f"Your HP: {player_hp}")
	print(f"{bossnames[boss_number]}'s HP: {boss_hp}")
	print("")
	while player_hp > 0 and boss_hp > 0 and talkSucc == False:
		if stabbed <= 0:
			while turnOver == False:
				# Player turn ADD DIFFERENT PRINTS and CHOICES DEPENDING ON INVENTORY!!!!!!!!!!!!
				#CODE BOSS DEFENSE!!!!!!
				#AND PLAYER BLEEDING
				if search_item(inventory, "burger"):
					if search_item(inventory, "shield"):
						print("Enter 'attack' to attack, 'defend' to defend, 'burger'to use a burger, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
					else:
						print("Enter 'attack' to attack, 'burger' to use burger, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
						choices[1] = "nothing"
				else:
					choices[2] = "nothing"
					if search_item(inventory, "shield"):
						print("Enter 'attack' to attack, 'defend' to defend, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
					else:
						print("Enter 'attack' to attack, or 'talk' to talk: ")
						print("Or type 'help' for stats or 'choices' for choices")
						choices[1] = "nothing"

				action = input("")
				print("")

				#attack
				if action == 'attack':
					#attackTypes = ["sweep","stab","slice","bash"]
					sweep = stats[AverageDamage] + 10
					stab = stats[AverageDamage] + 5
					slice = stats[AverageDamage]
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
					#bleeding lasts 3 turns
					#stabbed should equal two otherwise turn isnt missed
					if viewedAttacks == False:
						viewedAttacks = True
						print("Attack Types:")
						print("")
						print("Slider Sweep: An incredibly high damage and bloodletting attack with a somewhat high chance for the boss to dodge. Has a chance to cause dismemberment.")
						print("")
						print("Toothpick Stab: A high damage and bloodletting attack which can't be dodged. However, you have a chance to miss your next turn.")
						print("")
						print("Quickle Pickle Slice: An average attack with average damage. Low chance to be dodged. Causes bleeding on crit")
						print("")
						if search_item(inventory, "shield"):
							print("Shield Bash: A low damage attack that causes the boss to lose their turn. Average chance to be dodged. If dodged, this attack has a chance to count as a block.")
						print("")
						pause()
						print("Which attack would you like to do?")
					attackChoice = input("Type: 'sweep', 'stab', 'slice', or 'bash'. Or type 'choices' to view what each attack means.")
					print("")
					#sweep
					if attackChoice == "sweep":
						viewedAttacks = True
						dodge = random.randint(0,100)
						if dodge >= 60: 
							bossBleeding = 3
							damage_calc = random.randint(sweep-3,sweep+3)
							if damage_calc == sweep+3:
								player_attack = sweep+5
								print("Critical Hit!")
								dismemberChance = random.random() < 0.75
								if dismemberChance:
									dismembered = True
							elif damage_calc == sweep-3:
								player_attack = sweep-3
								print("Crappy Hit!")
							else:
								if damage_calc >= sweep:
									print("Great Hit!")
								elif damage_calc < sweep:
									print("Good Hit!")
								player_attack = damage_calc
							boss_hp -= player_attack
							print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
						else:
							print(f"{bossnames[boss_number]} dodged your attack!")
						turnOver = True

					#stab
					if attackChoice == "stab":
						viewedAttacks = True
						damage_calc = random.randint(stab-3,stab+3)
						bossBleeding = 3
						if damage_calc == stab+3:
							player_attack = stab+5
							print("Critical Hit!")
						elif damage_calc == stab-3:
							player_attack = stab-5
							print("Crappy Hit!")
						else:
							if damage_calc >= stab:
								print("Great Hit!")
							elif damage_calc < stab:
								print("Good Hit!")
							player_attack = damage_calc
						boss_hp -= player_attack
						print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
						stabChance = random.random() < 0.5
						if stabChance:
							stabbed=2
							print(f"Your {itemNames[1]} got lodged in {bossnames[boss_number]}! You miss your next turn.")
						turnOver = True

					#slice
					if attackChoice == "slice":
						damage_calc = random.randint(slice-3,slice+3)
						dodge = random.randint(0,100)
						if dodge >= 20:
							if damage_calc == slice+3:
								player_attack = slice+5
								print("Critical Hit!")
							elif damage_calc == slice-3:
								player_attack = slice-5
								print("Crappy Hit!")
							else:
								if damage_calc >= slice:
									print("Great Hit!")
								elif damage_calc < slice:
									print("Good Hit!")
								player_attack = damage_calc
							boss_hp -= player_attack
							print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
						elif dodge < 20:
							print(f"{bossnames[boss_number]} dodged your attack!")
						turnOver = True

					#bash
					if attackChoice == "bash":
						viewedAttacks = True
						dodge = random.randint(0,100)
						if dodge >= 40:
							print("Great Hit!")
							player_attack = 3
							boss_hp -= player_attack
							print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
							stunned = 1
							print(f"{bossnames[boss_number]} is stunned! {bossnames[boss_number]} misses their next turn.")
						elif dodge < 40:
							print(f"{bossnames[boss_number]} dodged your attack!")
							bestOffence = random.randint(0,100)
							if bestOffence <= 55:
								print("Even though you missed your attack, you ready your guard!")
								defending = True
						turnOver = True

					if attackChoice == "choices":
						print("Attack Types:")
						print("Big Sweep: An incredibly high damage and bloodletting attack with a somewhat high chance for the boss to dodge. Has a chance to cause dismemberment.")
						print("Stab: A high damage and bloodletting attack which can't be dodged. However, you have a chance to miss your next turn.")
						print("Quick Slice: An average attack with average damage. Low chance to be dodged. Causes bleeding on crit")
						print("Shield Bash: A low damage attack that causes the boss to lose their turn. Average chance to be dodged. If dodged, this attack has a chance to count as a block.")
						print("Which attack would you like to do?")
						viewedAttacks = True

				#defend
				elif action == 'defend':
					# Player defends
					print(f"You brace for {bossnames[boss_number]}'s attack.")
					defending = True
					turnOver = True

				#talk
				elif action == 'talk':
					if hasTalked == False:
						# Player attempts to talk
						success = random.random() <= 0.13
						if success:
							successMessage = random.random()
							if successMessage <= 0.33:
								print(f"You hide from {bossnames[boss_number]} ┬┴┬┴┤(･_├┬┴┬┴ you manage to escape")
								talkSucc = True
								stunned = 2
								break
							elif successMessage <= 0.66:
								print(f"You run away C= C= C= C=┌( `ー´)┘ you feel like a coward but you're still alive")
								talkSucc = True
								stunned = 2
								break
							elif successMessage <= 1:
								print(f"You beat {bossnames[boss_number]} in a game of rock-paper-scissors. They are legaly required to give up.")
								talkSucc = True
								stunned = 2
								break
							else:
								print("You successfully talked your way out of a fight. Nice.")
								talkSucc = True
								stunned = 2
								break
						else:
							print(f"Your attempt to talk failed. Now {bossnames[boss_number]} really hates you.")
							turnOver = True
						hasTalked = True
					else:
						print(f"{bossnames[boss_number]} already hates you. Try something else.")
				
				#misc
				elif action == 'burger':
					print(f"Burger%: {burgerPercent}")
					print("2% of a burger heals for 1 hp.")
					print("Hint: Eating more burger than needed to fill up your health to 100 will give you BurgerHealth")
					print("BurgerHealth depletes twice as fast.")
					print("How much of your burger do you want to eat")
					burgerAmount = int(input(""))
					if burgerAmount > burgerPercent:
						print("You dont even have that much burger!")
					elif burgerAmount <= 0:
						print("You cant eat that little burgers!")
					elif burgerAmount>0:
						print(f"You eat {burgerAmount}% burgers")
						burgerPercent-=burgerAmount
						stats[BurgerP]=burgerPercent
						burgerAmount=int(burgerAmount/2)
						player_hp+=burgerAmount
				elif action == 'help':
					help()

				elif action == 'choices':
					print(choices)
				elif action == 'quit':
					break
					choice = 'quit'
				
		else:
			print("")
			print(f"You retrieve your {itemNames[1]}, but you miss your attack as a result.")
		print("")

		# Boss attacks
		#CODE BOSS DEFENSE!!!
		#ALSO CODE DIFFERENT BOSS ATTACK
		#bossnames = ["Phil W. Frencherfrie","south","east","west","Zomburger"]
		
		if attackCharging == False:
			attackTypeBoss = random.random()
			if boss_number == 0:
				#phil
				if attackTypeBoss <= 0.80:
					bossDamage = random.randint(boss_attack-1,boss_attack+1)
					print("Phil swings his Burger Buster Sword!")
				else:
					print("Phil readies his Condiment Beam!!! However, he is unable to attack while charging.")
					bossDamage = random.randint(boss_attack, boss_attack+5)
					stunned = 1
					attackCharging = True
			if boss_number == 4:
				#zomburger
				if attackTypeBoss <= 0.80:
					bossDamage = random.randint(boss_attack-1,boss_attack+1)
			else:
				bossDamage = boss_attack
		if dismembered == True:
			bossDamage-=int(bossDamage/3)
		if stunned <= 0:
			attackCharging = False
			#DEFENDING
			if defending == True:
				#HAS ARMOR
				if player_armor > 0:
					damage_taken = int(bossDamage /2)
					player_armor -= damage_taken
					print(f"{bossnames[boss_number]} hits you for {damage_taken} damage! Your armor takes the hit!")
					stats[Armor] = player_armor
				#NO ARMOR
				else:
					#HAS BURGERHEALTH
					if player_hp > 100:
						damage_taken = int(bossDamage)
						player_hp -= damage_taken
						print(f"You have {int(player_hp-100)} BurgerHealth!")
						print(f"{bossnames[boss_number]} hits you for {damage_taken} damage!")
						if player_hp < 100:
							player_hp+=int((100-player_hp)/2)
						stats[Health] = player_hp
					#NO BURGERHEALTH
					else:
						damage_taken = int(bossDamage/2)
						player_hp-=damage_taken
						print(f"{bossnames[boss_number]} hits you for {damage_taken} damage!")
						stats[Health] = player_hp
				defending = False


			else:
				#HAS ARMOR
				if player_armor > 0:
					damage_taken = int(bossDamage)
					player_armor -= damage_taken
					print(f"{bossnames[boss_number]} hits you for {damage_taken} damage. Your armor takes the hit!")
					stats[Armor] = player_armor
				#NO ARMOR
				else:
					#HAS BURGERHEALTH
					if player_hp > 100:
						damage_taken = int(bossDamage*2)
						player_hp-=damage_taken
						print(f"You have {int(player_hp-100)} BurgerHealth!")
						print(f"{bossnames[boss_number]} hits you for {damage_taken} damage!")
						if player_hp < 100:
							player_hp+=int((100-player_hp)/2)
						stats[Health] = player_hp
					#NO BURGERHEALTH
					else:
						damage_taken = int(bossDamage)
						player_hp-=damage_taken
						print(f"{bossnames[boss_number]} hits you for {damage_taken} damage!")
						stats[Health] = player_hp
		else:
			if talkSucc != True:
				print(f"{bossnames[boss_number]} is still stunned!")
			else:
				print("talk suycceas")
		turnOver = False
		if stabbed > 0:
			stabbed-=1
		if stunned > 0:
			stunned-=1
		if bossBleeding > 0:
			bossBleeding-=1
			boss_hp-=6
			print(f"{bossnames[boss_number]} took 6 damage from bleeding!")
		if playerPoisoned > 0:
			playerPoisoned-=1
			player_hp-=6
		stats[Health] = player_hp
		stats[Armor] = player_armor
		stats[BurgerP] = burgerPercent
		print("")
		print(f"Your HP: {player_hp}")
		print(f"Boss HP: {boss_hp}")
		pause()
	if player_hp <= 0:
		stats[Health] = 0
		print(f"You have been defeated by {bossnames[boss_number]}.")
	elif boss_hp <= 0 or talkSucc == True:
		print(f"You have defeated {bossnames[boss_number]}!")
		bossnames[boss_number] = "dead"
		if stats[BurgerP] < 100:
			print("Your burger has been refilled!")
		coinDrop = random.randint(0,101)
		print(f"You got {coinDrop} BurgerBux!")
		
		#REFILL POTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#help

skipintro = input("skip intro? y/n")

#intro
if skipintro != 'y':
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
	print('"There is no sauce on my burger!!!" the Karen blabbed, completely oblivius to the fact that you put the sauce on the burger yourself.')
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

#tutorial
for i in range(1):
	print('')
	print('')
	print('!!!!!')
	print("IMPORTANT TUTORIAL and cool tips PLEASE READ:")
	print('')
	print("you can type 'help' at any time to view your inventory and stats")
	print("you can also type 'choices' at any time to view your choices")
	print("you can ALSO type 'inventory' to inspect your inventory items.")
	print('')
	print("TIP: Type 'choices' every time you enter a new room/environment. This can be very helpful(unless if youre a true burgergamer).")
	print('')
	print('!!!!!')
	print('')
	print('')
	pause()

#this is for the random monster encounters
monsterRooms = ["false","false","false","false"]
#1,5,9 is room 20
#2,6,10 is room 30
#3,7,11 is room 40
#4,8,12 is room 50
#maybe code multiple monster fights eventually
for i in range(4):
	monChance = random.randint(1,5)
	#print(placeholder)
	##room 20
	if monChance == 1:
		monsterRooms[0] = "true"
	##room 30
	if monChance == 2:
		monsterRooms[1] = "true"
	##room 40
	if monChance == 3:
		monsterRooms[2] = "true"
	##room 50
	if monChance == 4:
		monsterRooms[3] = "true"


def bigbooty():
	if choice == 'help':
		help()
	if choice == 'choices':
		print(choices)
	if choice == 'mon':
		print(monsterRooms)
	if choice == 'fight':
		fightChoice = input("custom or set fight")
		if fightChoice == "custom":
			bhp = int(input("Boss HP:"))
			ba = int(input("Boss Attack:"))
			bn = int(input("Boss number:"))
			boss_fight( bhp, ba, bn,)
		if fightChoice == "set":
			boss_fight(zomburger[0],zomburger[1],zomburger[2])
	print("")

while True:
	if room == 10:
		choices = "north, south, east, west, help, choices"
		print("You are in a grand hall.")
		print(" There are four doors to north, east, south, and west respectively.")
		choice = input("")
		bigbooty()

		if choice == 'break' or choice == 'quit':
			break
		if choice == 'north':
			room = 20

	if room == 20:
		if monsterRooms[0] == "true":
			monChance = random.random()
			if monChance <= 0.5:
				print("a Zomburger attacks ヽ( ￣Д￣)ノ <(burrrrgurzzzz)")
				boss_fight(zomburger[0],zomburger[1],zomburger[2])
			if monChance > 0.5:
				print("a Cheese Cat-Slime attacks (=^･ｪ･^=) <(mrowww)")
				boss_fight(slime[0],slime[1],slime[2])

		choices = "north, south, east, door, help, choices"
		print("You are in a dark, damp hallway. There is a very cool looking door to the east. To the north lies a very large door made with a strange red wood. or its just painted. A comically large golden burger shaped lock adorns the face of the door.")
		choice = input("")
		bigbooty()
		if choice == 'break' or choice == 'quit':
			break
		if choice == 'north' or choice == 'door':
			if keypieces == 4:
				#unlock door and enter boss room
				print("You approach the door. With the power of burger magic, the 4 key pieces fuse together.")
				print("The key has a beautiful golden burger-shaped emblem, with ruby gems the color of fine ketchup.")
				room = 23
			else:
				choices = "inspect, open, back, help, choices"
				print("A faint smell of rancid ketchup wafts through the cracks in the door.")
				choice = input("")
				bigbooty()
				if choice == 'inspect':
					print("You peer through the cracks in the door The other side is dark so you can't see anything.")
				if choice == 'open':
					print("You check the burgerlock(tm) lock on the door. its locked.")
				if choice == 'back':
					choice = "placeholder"
		if choice == 'east':
			room = 21
		if choice == 'south':
			room = 10
	if room == 21:
		#shield
		choices = "west, chest, open"
		if search_item(inventory,"shield"):
			print("The room is dark because you already opened the chest you doofus.")
		else:
			print("You enter a very dark room. There is a spotlight on the ceiling, aiming directly down at a very cool looking chest. You can't see anything else.")
		choice = input("")
		bigbooty()
		if choice == 'west':
			room = 20
		if choice == 'chest' or choice == 'open':
			if search_item(inventory,"shield"):
				print("The chest is empty")
			else:
				print(f"You open the chest. Inside the chest lies a {itemNames[shieldN]}!")
				inventory[shieldN] = "shield"
	monRoom = False
	if room == 22:
		#monster fight room (secret)
		monRoom = True
		bhp = int(input("Boss HP:"))
		ba = int(input("Boss Attack:"))
		bn = int(input("Boss number:"))
		boss_fight( bhp, ba, bn)
	if room == 23:
		#final boss room
		#locked (4 keys needed
		choice = input("")
		bigbooty()
	if room == 24:
		choice = input("")
		bigbooty()
	if room == 30:
		choice = input("")
		bigbooty()
	if room == 31:
		#shop room
		choice = input("")
		bigbooty()
	if room == 32:
		choice = input("")
		bigbooty()
	if stats[Health] <= 0:
		print("add save states pls")


print("")
print("No, you’re NOT a real gamer.")
print("")
print("I’m so sick of all these people that think they’re gamers. No, you’re not. Most of you are not even close to being gamers.I see these people saying “I put well over 100 hours in this game, it’s great!” that’s nothing, most of us can easily put 300+ hours in all our games.I see people who only have a Nintendo Switch and claim to be gamers. Come talk to me when you pick up a PS4 controller then we be friends.")
print("Also DEAR ALL WOMEN: Pokémon is not a real game. Animal Crossing is not a real game. The Sims is not a real game. Mario is not a real game. Stardew valley is not a real game. Mobile games are NOT.REAL.GAMES. put down the baby games and play something that requires challenge and skill for once.")
print("")
print("Sincerely, all of the ACTUAL gamers.")