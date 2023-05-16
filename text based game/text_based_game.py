import random
import time as t
from playsound import playsound
def pause():
	print("")
	programPause = input("Press <ENTER> to continue...")
	print("")
def blank():
	print("")
#https://www.geeksforgeeks.org/play-sound-in-python/#
#PLAY SPUIND FEFFEFTT
#other things



room = 10
choice = "PLACEHOLDER"
lost = False
won = False
vineBurn = False
boughtKey = False
burgerStock = 5
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
bossnames = ["Phil W. Frencherfrie","Patty Clown Kidnapper","Mouse with Sewing Needle","Really Big Cheese Cat-Slime","Zomburger","Cheese Cat-Slime"]
zomburger = [healthRand(70,90), 10, 4]
slime = [healthRand(30,50),20,5]
bigSlime = [healthRand(80,110), 30, 3]
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
	stunned = -1
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

				action = input("> ")
				print("")

				#attack
				if action == 'attack':
					print(f"stun: {stunned}")
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
							print("Shield Bash: A low damage attack that causes the boss to lose their turn GIVING YOU A GUARENTEED HIT. Average chance to be dodged. If dodged, this attack has a chance to count as a block.")
						pause()
						print("Which attack would you like to do?")
					print("Type: 'sweep', 'stab', 'slice', or 'bash'. Or type 'choices' to view what each attack means.")
					attackChoice = input("> ")
					print("")
					#sweep
					if attackChoice == "sweep":
						viewedAttacks = True
						if stunned == -1:
							dodge = random.randint(0,100)
						else:
							dodge = 100
						if dodge >= 60: 
							bossBleeding += 3
							damage_calc = random.randint(sweep-3,sweep+3)
							if damage_calc == sweep+3:
								player_attack = sweep+5
								print("Critical Hit!")
								playsound('criticalhit.mp3')
								dismemberChance = random.random() < 0.75
								if dismemberChance:
									dismembered = True
							elif damage_calc == sweep-3:
								player_attack = sweep-3
								print("Crappy Hit!")
								playsound('crappyhit.mp3')
							else:
								if damage_calc >= sweep:
									print("Great Hit!")
									playsound('criticalhit.mp3')
								elif damage_calc < sweep:
									print("Good Hit!")
									playsound('normalhit.mp3')
								player_attack = damage_calc
							boss_hp -= player_attack
							print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
						else:
							print(f"{bossnames[boss_number]} dodged your attack!")
							playsound('woops.mp3')
						turnOver = True

					#stab
					if attackChoice == "stab":
						viewedAttacks = True
						damage_calc = random.randint(stab-3,stab+3)
						bossBleeding = 3
						if damage_calc == stab+3:
							player_attack = stab+5
							print("Critical Hit!")
							playsound('criticalhit.mp3')
						elif damage_calc == stab-3:
							player_attack = stab-5
							print("Crappy Hit!")
							playsound('crappyhit.mp3')
						else:
							if damage_calc >= stab:
								print("Great Hit!")
								playsound('criticalhit.mp3')
							elif damage_calc < stab:
								print("Good Hit!")
								playsound('normalhit.mp3')
							player_attack = damage_calc
						boss_hp -= player_attack
						print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
						stabChance = random.random() < 0.5
						if stabChance:
							stabbed=2
							print(f"Your {itemNames[1]} got lodged in {bossnames[boss_number]}! You miss your next turn.")
							playsound('woops.mp3')
						turnOver = True

					#slice
					if attackChoice == "slice":
						viewedAttacks = True
						if stunned == -1:
							dodge = random.randint(0,100)
						else:
							dodge = 100
						if dodge >= 20:
							damage_calc = random.randint(slice-3,slice+3)
							if damage_calc == slice+3:
								player_attack = slice+5
								print("Critical Hit!")
								playsound('criticalhit.mp3')
							elif damage_calc == slice-3:
								player_attack = slice-5
								print("Crappy Hit!")
								playsound('crappyhit.mp3')
							else:
								if damage_calc >= slice:
									print("Great Hit!")
									playsound('normalhit.mp3')
								elif damage_calc < slice:
									print("Good Hit!")
									playsound('normalhit.mp3')
								player_attack = damage_calc
							boss_hp -= player_attack
							print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
						elif dodge < 20:
							print(f"{bossnames[boss_number]} dodged your attack!")
							playsound('woops.mp3')
						turnOver = True

					#bash
					if attackChoice == "bash":
						viewedAttacks = True
						if stunned == -1:
							dodge = random.randint(0,100)
						else:
							dodge = 100
						if dodge >= 60:
							print("Great Hit!")
							playsound('bonk.mp3')
							player_attack = 3
							boss_hp -= player_attack
							print(f"You hit {bossnames[boss_number]} for {player_attack} damage!")
							if stunned == -1:
								stunned = 1
								print(f"{bossnames[boss_number]} is stunned! {bossnames[boss_number]} misses their next turn.")
						elif dodge < 60:
							print(f"{bossnames[boss_number]} dodged your attack!")
							playsound('woops.mp3')
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
					playsound('ham.mp3')
					print(f"Burger%: {burgerPercent}")
					print("2% of a burger heals for 1 hp.")
					print("Hint: Eating more burger than needed to fill up your health to 100 will give you BurgerHealth")
					print("BurgerHealth depletes twice as fast.")
					print("How much of your burger do you want to eat")
					burgerAmount = int(input("> "))
					if burgerAmount > burgerPercent:
						print("You dont even have that much burger!")
					elif burgerAmount <= 0:
						print("You cant eat that little burgers!")
					elif burgerAmount>0:
						print(f"You eat {burgerAmount}% burgers")
						playsound('burger.mp3')
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
				elif action == 'instakill':
					boss_hp = 0
		else:
			print("")
			print(f"You retrieve your {itemNames[1]}, but you miss your attack as a result.")
		print("")

		# Boss attacks
		#CODE BOSS DEFENSE!!!
		#ALSO CODE DIFFERENT BOSS ATTACK
		#bossnames = ["Phil W. Frencherfrie","south","east","west","Zomburger"]
		if boss_hp > 0 or talkSucc != True:
			if stunned == -1:
				if attackCharging == False:
					attackTypeBoss = random.random()
					if boss_number == 0:
						#phil
						if attackTypeBoss <= 0.80:
							bossDamage = random.randint(boss_attack-1,boss_attack+3)
							print("Phil swings his Burger Buster Sword!")
						else:
							print("Phil readies his Condiment Beam!!! However, he is unable to attack while charging.")
							bossDamage = random.randint(boss_attack, boss_attack+5)
							stunned = 1
							attackCharging = True
					else:
						bossDamage = random.randint(boss_attack-1,boss_attack+2)
						if attackTypeBoss <= 0.20:
							attackword = "swipes"
						elif attackTypeBoss <= 0.40:
							attackword = "swings"
						elif attackTypeBoss <= 0.60:
							attackword = "pounces"
						elif attackTypeBoss <= 0.80:
							attackword = "strikes"
						else:
							print(f"{bossnames[boss_number]} charges a strong attack at you. However, they is unable to attack while charging.")
							bossDamage = random.randint(boss_attack, boss_attack+5)
							stunned = 1
							attackCharging = True
						if attackCharging != True:
							print(f"{bossnames[boss_number]} {attackword} at you")
							playsound('bosshit.mp3')

			if dismembered == True:
				bossDamage-=int(bossDamage/3)
			if stunned == -1:
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
			if stunned >= 0:
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
		playsound('lose.mp3')
	elif boss_hp <= 0 or talkSucc == True:
		print(f"You have defeated {bossnames[boss_number]}!")
		playsound('win.mp3')
		bossnames[boss_number] = "dead"
		if stats[BurgerP] < 100:
			print("Your burger has been refilled!")
		coinDrop = random.randint(80,250)
		print(f"You got {coinDrop} BurgerBux!")
		stats[BurgerBux] += coinDrop
		
#REFILL POTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#help

print("skip intro?")
print("y/n")
skipintro = input("> ")

#intro
if skipintro != 'y':
	print('')
	print("welcome to BurgerQuest")
	pause()
	print("Our main character is Stephen H. Burgerguy, a burger shop owner and chef.")
	pause()
	print("Stephen was a normal guy, flipping burgers and cooking burgers and eating burgers")
	pause()
	print("Until one day, that all changed.")
	pause()
	print("A jerkhole customer decided to complain about Stephens flawless burgers!!!")
	pause()
	print('"There is no sauce on my burger!!!" the Karen blabbed, completely oblivius to the fact that you put the sauce on the burger yourself.')
	print("(what an idiot, am i right?)")
	pause()
	print("After this incident, annoying customers started showing up week after week,")
	pause()
	print("day by day,")
	pause()
	print("hour by hour,")
	pause()
	print("minute by minute.")
	pause()
	print("Burgerguy grew tired of these annoying customers.")
	pause()
	print("Stephen did some research (on twitter), and it turned out that he had been cursed by the evil BurgerKing,	who resides within a burger dungeon!")
	pause()
	print("The Burger King was mad that Stephen's burgers were better than his (what a jerk).")
	pause()
	print("So, Stephen, with his trusty sword (that he bought off craigslist), enters the dungeon to take the Burger King on")
	pause()
	print("So begins, BurgerQuest")
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

printrooms = ['n']
def bigbooty():
	if choice =='print rooms':
		printrooms[0] = 'y'
	if printrooms[0] == 'y':
		print(room)
	if choice == 'help':
		help()
	if choice == 'choices':
		print(choices)
	if choice == 'mon':
		print(monsterRooms)
	if choice == 'fight':
		print("custom or set fight")
		fightChoice = input("> ")
		if fightChoice == "custom":
			bhp = int(input("Boss HP:"))
			ba = int(input("Boss Attack:"))
			bn = int(input("Boss number:"))
			boss_fight( bhp, ba, bn,)
		if fightChoice == "set":
			boss_fight(zomburger[0],zomburger[1],zomburger[2])
	if choice == 'money':
		print("how much money")
		moneyadd = int(input(""))
		stats[BurgerBux] += moneyadd
	if choice == 'sound':
		print("bonk/shieldbash")
		playsound('bonk.mp3')
		print("boss hit")
		playsound('bosshit.mp3')
		print("burger eat")
		playsound('burger.mp3')
		print("crappy hit")
		playsound('crappyhit.mp3')
		print("critical hit")
		playsound('criticalhit.mp3')
		print("normal hit")
		playsound('normalhit.mp3')
		print("dodged")
		playsound('woops.mp3')
		print("burger select")
		playsound('ham.mp3')
		print("win")
		playsound('win.mp3')
		print("lose")
		playsound('lose.mp3')
		print("item get")
		playsound('itemget.mp3')
	print("")
	

while True:
	if room == 10:
		choices = "north, west, east, south, help, choices"
		print("You are in a grand hall.")
		print("There are four doors to north, east, south, and west respectively.")
		blank()
		choice = input("> ")
		bigbooty()
		if choice == 'room':
			roomPick = int(input("which room would you like to go to: "))
			room = roomPick
		elif choice == 'break' or choice == 'quit':
			break
		elif choice == 'north':
			room = 20
		elif choice == 'west':
			room = 30
		elif choice == 'east':
			room = 40
		elif choice == 'south':
			room = 50
		else:
			print("stupid.")
			choice = "placeholder"

	if room == 20:
		#prev room = 10
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
		blank()
		choice = input("> ")
		bigbooty()
		if choice == 'break' or choice == 'quit':
			break
		elif choice == 'north' or choice == 'door':
			if keypieces == 4:
				#unlock door and enter boss room
				print("You approach the door. With the power of burger magic, the 4 key pieces fuse together.")
				print("The key has a beautiful golden burger-shaped emblem, with ruby gems the color of fine ketchup.")
				room = 23
			else:
				choices = "inspect, open, back, help, choices"
				print("A faint smell of rancid ketchup wafts through the cracks in the door.")
				blank()
				choice = input("")
				bigbooty()
				if choice == 'inspect':
					print("You peer through the cracks in the door The other side is dark so you can't see anything.")
				elif choice == 'open':
					print("You check the burgerlock(tm) lock on the door. its locked.")
				elif choice == 'back':
					choice = "placeholder"
				else:
					print("stupid.")
					choice = "placeholder"
		elif choice == 'east':
			room = 21
		elif choice == 'south':
			room = 10
		else:
			print("stupid.")
			choice = "placeholder"
	#shield
	if room == 21: #shield
		#prev room = 20
		choices = "west, chest, open"
		if search_item(inventory,"shield"):
			print("The room is dark because you already opened the chest you doofus.")
		else:
			print("You enter a very dark room. There is a spotlight on the ceiling, aiming directly down at a very cool looking chest. You can't see anything else.")
		blank()
		choice = input("> ")
		bigbooty()
		if choice == 'west':
			room = 20
		if choice == 'chest' or choice == 'open':
			if search_item(inventory,"shield"):
				print("The chest is empty")
			else:
				print(f"You open the chest. Inside the chest lies a {itemNames[shieldN]}!")
				playsound('itemget.mp3')
				inventory[shieldN] = "shield"
	monRoom = False
	if room == 22: #monster fight room (secret)
		monRoom = True
		bhp = int(input("Boss HP:"))
		ba = int(input("Boss Attack:"))
		bn = int(input("Boss number:"))
		boss_fight( bhp, ba, bn)
	#final boss
	if room == 23: #final boss room
		#locked (4 keys needed)
		blank()
		choice = input("")
		bigbooty()
	if room == 24:
		print("This is it.")
		pause()
		print("You have reached the end ")
		pause()
		print("You defeated the Burger King, and now", end = "")
		t.sleep(0.4)
		print(".",end = " ")
		t.sleep(0.4)
		print(".",end = " ")
		t.sleep(0.4)
		print(".")
		pause()
		print("Your ", end ="")
		t.sleep(0.3)
		print("B", end = "")
		t.sleep(0.3)
		print("U", end = "")
		t.sleep(0.3)
		print("R", end = "")
		t.sleep(0.3)
		print("G", end = "")
		t.sleep(0.3)
		print("E", end = "")
		t.sleep(0.3)
		print("R", end = "")
		t.sleep(0.3)
		print("Q", end = "")
		t.sleep(0.3)
		print("U", end = "")
		t.sleep(0.3)
		print("E", end = "")
		t.sleep(0.3)
		print("S", end = "")
		t.sleep(0.3)
		print("T", end = " ")
		t.sleep(0.3)
		print("is over.")
		pause()
		print("Would you like to remain in the dungeon?")
		print("y/n")
		blank()
		choice = input("> ")
		if choice == "y":
			room = 10
		if choice == "n":
			break
		else:
			print("stupid.")
			choice = "placeholder"
	#puzzle
	if room == 30: #puzzle
		choices = 'east, south, use, west, door, vines, help, choices'
		print('You are in an overgrown room, covered with vines. There are two doors. The door to the West in locked shut by the vines. The door to the left has a bright neon sign saying "SHOP"')
		blank()
		choice = input("> ")
		bigbooty()
		if choice == "east":
			room = 10
		elif choice == "south" or choice == "shop":
			room = 31
		elif choice == "use" or choice == "vines" or choice == "west" or choice == "door":
			if vineBurn == True:
				print("You enter the room.")
				room = 32
			if vineBurn == False:
				print("These vines are blocking the westward door. Maybe you can destroy them somehow. wink wink")
				blank()
				choice = input("> ")
				bigbooty()
				if choice == 'torch' or choice == 'burn':
					print("You burn down the vines, opening the way!")
					vineBurn = True
					room = 32
				if choice == 'cut' or choice == 'sword':
					print("You cut the vines, opening the way!")
					blank()
					vineBurn = True
		else:
			print("stupid.")
			choice = "placeholder"
	if room == 31: #shop room
		choices = 'key piece, burger, leave, north'
		print("You enter the shop")
		print('"Hello!" says the shopkeeper, a sentient French Fry.')
		print("What would you like to buy:")
		print("")
		if boughtKey == False:
			print("Key Piece, 300 BurgerBux")
		else:
			print("Key Piece, out of stock")
		if burgerStock >0:
			print("Burger, 50 BurgerBux")
			print(f"Burgers left in stock: {burgerStock}")
		else:
			print("Burgers, out of stock")
		blank()
		choice = input("> ")
		bigbooty()
		if choice == 'leave' or choice == 'north':
			room = 30
		elif choice == 'key piece' or choice == 'key':
			if boughtKey == True:
				print("out of stock!")
			elif stats[BurgerBux] >= 300:
				print("You bought the key piece.")
				print("-300 BurgerBux")
				blank()
				stats[BurgerBux] -= 300
				print(f"BurgerBux remaining {stats[BurgerBux]}")
			else:
				print("stupid. not enough money >:(")
				choice = "placeholder"
		elif choice == 'burger' or choice == 'hamburger':
			if burgerStock <= 0:
				print("out of stock!")
			elif stats[BurgerBux] >= 50:
				print("You bought a Burger.")
				print("-50 BurgerBux")
				blank()
				stats[BurgerBux] -= 50
				print(f"BurgerBux remaining {stats[BurgerBux]}")
			else:
				print("stupid. not enough money >:(")
				choice = "placeholder"
		else:
			print('spupid')
			choice = "placeholder"
		blank()
	if room == 32: #boss
		print("Its full of artisan cheese and also some peanut butter.")
		blank()
		if bossnames[rat[2]] != "dead":
			print(f"A large Mouse with a Sewing Needle Attacks!")
			boss_fight(rat[0],rat[1],rat[2])
			print("A chest appears, and you open it.")
			print("You get the Sewing Needle of Death!!!")
			playsound('itemget.mp3')
			#itemNames = ["Grease Torch","Fry Sword","Burger Bun Armor","Pickle Shield","Burger","Key Piece"]
			itemNames[swordN] = "Sewing Needle of Death"
			stats[AverageDamage] = 15
		else:
			print("There's nothing here:")
			room = 30
		
	if room == 40:
		print("")
	if stats[Health] <= 0:
		print("add save states pls")



#("No, you’re NOT a real gamer.")

#("I’m so sick of all these people that think they’re gamers. No, you’re not. Most of you are not even close to being gamers.I see these people saying “I put well over 100 hours in this game, it’s great!” that’s nothing, most of us can easily put 300+ hours in all our games.I see people who only have a Nintendo Switch and claim to be gamers. Come talk to me when you pick up a PS4 controller then we be friends.")

#("Also DEAR ALL WOMEN: Pokémon is not a real game. Animal Crossing is not a real game. The Sims is not a real game. Mario is not a real game. Stardew valley is not a real game. Mobile games are NOT.REAL.GAMES. put down the baby games and play something that requires challenge and skill for once.")

#("Sincerely, all of the ACTUAL gamers.")

#      ...........  .... ............................................ ..... ..........................              .    ........',
#       ..... ....  .... ............................................ ..... .....................                        ........',
#          .   ...  ....  ........................................... ....  ................                             ........',
#              ..   ....  ...........................................  ...   ............                                ........',
#               .    ...   ...........',,;;::ccclcc::::::;;;,,,''....  ...   .  ..                                       ........',
#                    ..    .    .';:loddxxxkOOkkkkkkxxxxxxxxxdddddoolc:;,'...                                            ........',
#                             .;ldxxxxxxxxxkkOkkOOkxxdddxxxxxddodxxxxdooooolc:;,..                                       ........',
#                           .;oxxxxkkkkxxkkkkkkkkxxxxxdddddxxxddddxxxxddooooooodoc:,..                                   ........',
#                          .cxxkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxxxxxxxddoooooooddoc:,..                               ........',
#                         .:kkkkkkkkOOOOOkkkOkkkkkkkkxxxxkxxxxxxxxxxxxddxxddddodxddooddolc;.                             ........',
#,'.                      ;kOkkkkOOOOOOOOOOOOOOOkkkkkkkkxxxxxxxxxkkxxxddddddooooooooooddoolc'.                           .......'',
#.;;,.                   .oO0OOOOOOOOOOOOOOOOOOOOOkkkkxxxxxxxxxxxxdooddddoolllllcloddodxdolc::c;'.                       .......'',
# .;;;'.                 ;xkO00OOOOOOOOOOOOOOOOOOkkkkxxxxxxxdddxxolccodoooolclcc:cclllool::c:;lxxdl;.                    .......'',
#  .,:;,.                ,odk0K000000OOOOOOOOOOOOkkxxxxxxxxxddddoolc:clolcllcccc:::::::::;;;;,;ldxxxdc,.                 .......'',
#   .,:::,'.     ....  .',:;ckO00000OOOOOOOOOOOOOkkxxxxxddddooooollccccllclolccc:::cc::;;;;;;,,;:oxxkxdl;.               .......'',
#     .;cccc:'....',,'',,',,;okxdddxxxxkkkkkkkkOkkkxxxxddddooooollccccclllddlllc::clllcccc:::;;,,:dkkxollc'.             .......'''
#      .',:cllcc:;,,;::;,,:::dOkdoc;,'',,;:cclodxxxxxxxdddooooolccclcccclodooolcclllllllccllc::;,:okkdc:ccc:.            .......'''
#          .';:cllllc:::;;:::oxxxkxo:,.........'',;::cccccclcllllllllc::cllolcloooollllllllllcc::coxxoc;;;::'            .......'''
#      ...     ..',;;::;;,;:odoccoddo:;,;,'.............. ......,;::c::::ccccccccllloooooollllc;,;:llc::::;;.           ........'''
#     ,llc:;;;,''.......';odxxocccclolcl:'.............         ............',;;;;;;;;;:::clll:,......''''....          .........''
#     .''',,,;;;;,''....'ldxxxdlc:;:loc:,,',;;cool:,...        ..........   .......       ...''.. ...........           .........''
#             ....     .cxxxxxxolc::cl:;:;;lddddlc;'....       .''......................           .....                .........''
#                       .,'',;clc::;;:c:;;:clooc;'......    .';:loolc:;;,,'''''''.......             ...'......          ..........
#                .....',,;;::clc'.,,,,;:;;:ccc::,'........':oddoodxxxxxxdddolllooc,....        .... ...cxxddddooollcc:;;;;,''......
#      ...',;:ccloddxxxxkkkkkkkxlc:;,,:oooddc;'';;;;;;;,,:ccodxxxxddddoooooooolll;...           .......;dxxxxkkkkkkkkkkkkkkkxxdoolc
#',;:loddxxxkkkkkxxxkkkkkkkkkkkkkdc:,,;::::,'..;ddooddddoc:,,;coxkkkkkxdddoool:'... ..............   ...,okxxxxkxkxxkkkkkkkkkkkkOOO
#xkkkkxxkkkkkkkkkkkkkkkkkkkkkkkkxoocclc;,'.....,lllodlc:;;;:,..':lodxxkxxxddoc;'....;;,,''...............,oddddddddxxxxxxxxkkkkkkkk
#kkkkkkkkkkkkkkkkkkkkkkkkkkxxxxxkO0kxxdc;,'...'cddddc,,;:codc.';:lllllldxxdoc:::;;:clc::;;,'..............;loooooooodddxxxxkkkkkkkk
#kkkkkkkkkkkkkkxxxxxxxxdddxxxdld000Okxddollcccoddlccccllccoc............,col:,.',;:ldddddddolc:;,'........',,;:clooddddddddxxxkkkkk
#kkkkkkkxxxxddddddodddddddddl;,o00000Oxddxxdooollllc:;,'....              .,'.     ..,:lodxxddooc:'..''''''''''',,;:cloddddddddxkkk
#kxxxdddooooooooooooddddxxxd:':x0000000kdddoolc;,...      ...  .   ......              ..,:ldxdooo:'..........''''''',;clodddddddxx
#dooollllllloooooddddxxxkkkxc;lO000000Okxoc;'..     .....',,,'''.. ...........     ...... ..';coddo:'..................',:loddddddd
#lcclllllloooodddxxxkkkkkOOo;,l0KK0Oxoc;'.....  ..'''','.'';:;;,.........'..... ............. .'codo:'...................',:loddddd
#ccclllloodddxxxkkkkOOOOOOOxl;oOOko:'..   .','',;:;;,'';;'',,''......''......................    .;oc'.','''''''''''''.....';codddd
#cccloooddxxkkkkOOOOOOOOOOkkdccclc;.. .. .,;,,,',;,'.';;'.','.........'..''..  ............       .',..';;...''''''',,,''....,clodd
#ccloddxxkkkOOOOOOOOOOO00Okkxlc::;,..... ..,'..',,;;,'..',;,',;,'''..'....................      ....',;:cc;............''''.',clood
#loodxxkkOOOOOOOOO0OOOO000OOkkdc;;,'..... .':;,;;;;;,'....;;',:;,'....  ..............      ...',;::clollc;.............',;:clloood
#odxxkkkOOO00000000000000000OOOdc:;,,'.....';,,;;,'.....'''...''............ .    ......',;::clloolllllc:;'......'',;:ccllloooooodx
#xxxkkOOO000000000000000000000O00Okxdol:;;,,,'',;;,........... ...... ......'',,;;:clllllooooollllc:;,''''...,:ccllloooooodddxxxxxk
#xkxkOOO00000000000000000KK0OO0000K00000OOOkxddddol:,',;;::::cccclllllloodxxxxdddddooooooooollc:,'..........':loooodxxxxxxkkkkkkkkO
#dxOOOOO0000000000000000KKKK0OOOOO0000000KKK0OOOOkxdooxkkOOOOOOOkkkkkkkxxxxdddddddddoooolc;,,.........''''''':loooodxkkkkkkOOOOOOOO
#dxkOOOO0000000000000000KKKKKKK0OkkkkkO0000OkkOOxdddddxxxxxxxxxdddddddddddddddddollc:;,'........',;:clooodddddxxxxkkkkkkOOOOOOOOOO0
#odxkkOOO0000000000000000KKKKKKKKK0Okxxddoodddxxkxxddddddddooddooooooollccc::;,,'.......',;::clodxxkkkkOOOOOOOOOOO00OOOOOO000000000
#dxxxxkkOO000000000000000KKKKKKKKKKKKK00Okxxxdxxxxxdoolllc:;;;,,,,,,'''......'',;::clodxxkOOOOOO00000000000000000000000000000000000
#kkxxxxkkOOOO0000000000000KKKKKKKKKKKKKKKKKKKKKKKK00OOkkkxddoooooooooddddddxxkkOOO00000000000000000000000000000000000000000000OOOOO
#kkkkkkkkkkkOOOO000000000000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0000000K000000000K000000000000000000000000000000000000OOOOOkkkkOO
#kkkkkkkkkkkkkkOOOOO000000000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKK00KKKK0KKK0KKKKKKKK00KKKKK00KKK00KKKKKKK000KK00000000OOOOOkkkkkkkkkkOOOO
#kkkkkkkkkkkkkkkkkkkOO0000000000000KKKKKKKKKKKKKKKKKK0000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK000000OOOOOOOkkkkkkkkkkkkkkkkkkOOOOO
#kkkkkkkkkkkkkkkkkkkO00000OOO00OOOOOO00000000KKKKKKKKKKKKKKKKKKKKK0KKKKKKKKKKKKKKKKK0000000OOOOkkkkkxxxxxkkkkkkkkkkkkkkkkkOOOOOOOOO



#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMM0lkWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMWx.oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMWl.lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMWl ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMNc ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMK, ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMK, ;KMMMMMMMMMMMMMMMMMMMMMMMNKkolc:co0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMO. ,0MMMMMMMMMMMMMMMMMMMMMKo;'',;::,..c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMx. .xNNNWMMMMMMMMMMMMMMMMNl.,ldxxxxdo:.:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMWKx:'',colloOWMMMMMMMMMMMMMMNc.lxxxxxxxxo'.xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMM0c;coddxxxo;cKMMMMMMMMMMMMMMNc.cxxxxxxxxxc.:XMMMMMMMMMMWWNNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMO:lxkkkkkkx:,cooooooooooodxOOc.'odddxxxxxl.,KMMMMMWKkxo:;:::;;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMO::dxxkkxdc,;:::::::::::;;,,;'...,'';:cc;..dNMMMMM0,.',;coooc..dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMNkc,,:cc:;;:oxxxxxxxxxxxxxxdddoollc;,..  .cONWMMMMk.,dxxxxxxxl.'OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMM0,.cllooddxxxxxxxxxxxxxxxxxxxxxxxxxdl:;,'',cONWMk.,dxxxxxxxo'.kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO' .,;;;;:cccoxxxxxxxxxxxxxxxxxxxxxxxxxxdo:.',;ll..lxxxxxxo,.:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMx..'.,o:. .;..;oxxxdocoxxxxxxxxxxxxxxxxxxxddlc:,.  'cdddc,..lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMd.:c.:0o.:0NKc.'ldxdl:lxxxxxxxxxxxxxxxxxxxxxxxxdoc;...'..;o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMWo.;l.'c.;KMMMNl..;dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl;..,xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMN:.:l..,.,cloxkc...'ldxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdo:'.;dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMX:.ll.,OKOxdollclOd..lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl,.'ckXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMK;.ll.,0MMMMMMMMMMWd.'oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxoc,.,cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMO''lo'.kMMMMMMMMMMMXc.:dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxocldxdo:..lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMO',oo;.xMMMMMMMMMMMMO''oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxocldxxxxo;.'xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMWx.,oo;.xMMMMMMMMMMMMX:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl'.lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMWo.:oo;.xMMMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo,.:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMWo.:do;.dWMMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo;.:0WMMMMMMMMMMMMMMMMMMMMWK0XWMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMNc.:oo:.cNMMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd:.,OWMMMMMMMMMMMMMMMMMMWk:,cKMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMK;.lodc.:KWMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdc..lXMMMMMMMMMMMMMMMMWO:;;:OMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMWx.'looc..,:ldO0KNWWWWX:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdo,.:KMMMMMMMMMMMMMMMXl;l;cKMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMO'.;oxo:..lxoccc::llllc..lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd;.lNMMMMMMMMMMMMMWk;cl;oNMMMMMMMMMMM
#MMMMMMMMMMMMMMMMNl.'lKMKl'.cNMMMWXKKKKKO;.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo'.dWMMMMMMMMMMMW0c;oc;kWMMMMMMMMMMM
#MMMMMMMMMMMMMMMMX:.,xWMWx,.:XMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl.'OMMMMMMMMMMMNd',:;cKMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMNc.'xWMWx,.:XMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd:.cXMMMMMMMMMWO;;c;;OWMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMWd..cKWKc..dWMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo'.xWMMMMMMMMXl;oo;oXMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMXl..:dc..cXMMMMMMMMMMMN:.lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc.'OMMMMMMMXd;co;:0WMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMNx;,,';xNMMMMMMMMMMMMK,.oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd:.;KMMMMMNd;cdc;xWMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMWXXXWMMMMMMMMMMMMMMO',dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd,.dWMMMWk,,::,lKMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.;dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc.;KMMNk::l;'lKWMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:.,oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd,.kWXo;:dl;lKMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;.;oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:.okc,cdo;cKMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.;dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:..;;;::;l0WMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:.'odc,,dXMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd;.:dl;cONMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo..,;:dXWMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.,dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:..ckXWMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,.;dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd;.dWMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,.'cdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxl.'OMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk;.'cdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd,.lNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,.,ldxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd;.,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,.';codxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdoc'.;0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOdc,'',;:clddxxxxxxxxxxxxxxxxxxxxxxxxxxxxddooc;,''':dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kdlc;,,',;;;;;;;;;;;;;;;;;;;;;;;;;;,',;,;coxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOxddxxxxxxxxxxxxxxxxxxxxxxxdxkKXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM


# .  .. .......                    ..........................      ......................................''''....,,...............'
#..................          ....,coddl:,',,,,'''''.......              .......';c:;'...................';:::,...''..',,'''...''..,
#...................         ...:dkkOOOko;,,,;:::,.....                      .;dO0Oxl;...................;cc:,...''..',,,,''...'..'
#.............          .  ....,looooddddc,:ldO00Od;.                .,cll:,.,oxddoooc,..................':lc,....,,'',,,,,''..'...
#.............           ......,cllllllllcclodxxkOOd,.              .ckOkxdoccllllccc:'...............'''';c:'....,,'',,,,,,'..'...
#..............      ..........';:cccccccccllllooodo;.              'lddollcccccccc::;..............''....'::.....''.',,,,,,'..''''
#.......;okkko:..   .........';,,;::cccccccccccccll:.               .;clccccccccccc:;..  ........'''..'''..',........',;;;,,'''''''
#.''...;dOOkxxdc'...........;cl:,';::ccccccccccc::;.                 ..,;;::cccccc:;'.     ..,codxxdc,'''.............',,,,,''''''.
#xxdl:,coooolllc;.........,:llll;'';::ccccccc::;,'.                     ..',;;::::;'.      .;okOO000Oxc'.''',:cc:,....',,,,,''',,..
#kxdoolcclccccc:,.......,:cllllc;..',;:ccc::;,'..     ....                 ...'','..      .,lddddddxxxo:',:ok0KKK0x:...',','''',,..
#olllccccccccc:;'.....';cllllcc:'...',;;;;,'..     ..',,,,'..    ....',''..    ....       .;lolllllloooc:codxxkkOOOk:..''''''',;:;'
#lccccccccccc::,....';:cllcc:cooc,...'''...       .',;;:cc:;'....',;:::;;;,.....          .,ccccccccccccclllooooddxxc'..''''';oxOOx
#;;:::ccccccc:;'...,cooolc;:dO0KK0o,....         ..';:ldddolc,.';clooddoc;,'...........   .';::ccccccccccccclllllloo:...''..,cooddx
#..',,;;:::::;'..':okOOkxlclddxk0Od:.           ...,:lloxkkxoc;:ldxxkxdooc,'................';;::ccccccccccccccccclc,...'''.,:cccll
#  ....'',,,,'..,:ldxxdooollllllool:.         .....':clxkkkkxoclxkOOOOkocc,...'''''..........',;::cccccccccccc::::;,;;;;;;;,';:cccc
#   ..........';ccclooolllcccccccc:,.       ........,:lddddoooooddddddxoc;'..'''''''''........',;::ccccccccc:::;;,,;:::::::;,,;:ccc
#  ..........,:ccc;;:ldkdolccccc::,.      .......'...,:llllllllllooooooc;'..,,,,'''''''''''....',;;:cccccc::;;,,,;::::::::::;,,;:cc
#...........;:cc:'..;d0XKOdlcc::;,.      .....''''''..';:clllllllllllc:,..',;,,,,,'''''''''''''.'',;::::::;,,,,;:::::::::::::;',;::
#..........,:c:,.  .'cdOOo:;:::;'.     ......'''',,,'...,;:ccllllccc:,'.',;;;;,,,,,,,,,,'''''','''',,;;;,''',;:::::clc::::::::;'',,
#',;;;;;,'..,,'.      .,:'.,,;,'.     ......''''',,,,,'..',;;:cc:;;,'.',;;;;;;;,,,,,,,,,,'',,,,,''.''''....';;;;;:ldkkd::::::::;,,;
#;;;;;;;;,,'...            .....      .....''''',,,,,,,,'..',,;,,....,;;;;;;;;;,,,,,,,,,,'',,,,,,''....   ..;;;;;cooodollool:::::::
#:loddolc;,'...                       .....''',,,,,,,,,;,,'..''...'',;;;;;;;;;;,,,,,,,,,,,,,,,,,,,''.     .';;;cdkOdclllok0Oo::::::
#dddddoool:,'..      ..'.            ......'',,,,,,,,,,,;,,,....',;;;,;,;;;;;;,,,,,,,,,,,,,,,,,,,'''..    .';;;:dkxoccccldkxl::::::
#odkkkxdllc;'..   .'.,ldl'          ......'''''',,,,,,,,;;;;;,,;;;;;;;;;;;;;;,,,,,,,,,,,,,''''''',,''.    .',;;;;;;::::::cc::::::::
#k000OOkdlc:,..  .cdlclcc'         ........'''',,,,,,',,,,,;;;;;::;;;;::;;;;;;;;;,,,,,,,,,,,,,''''','.    ..,;;;;;;;;;;;;;;;:::::::
#kkxxxdddoc;,..  .':::cc;.        .........''',,,,,'..........'',,,,;;;;;;;;;;;;;;;,;;;;,,,,,,,,,,'''.    ..,;;;;;;;;;;;;;;;;::::::
#oooooooolc;'.     ...''.         ........''',,'''...................',,;;;;;;;;;;;,,,,,,,,,'''''''''..  ...,;;;;;;;;;;;;;;;;::::::
#ooolllllc:,..                    .......',,,'''''.....................'',,,,,;;,,,,,,'''..............  ...,;;;;;;;;;;;;;;;;::::::
#llllllcc:,..   ..                 .....',,,',''',,,,,,,'''''................'''''''.................... ...,,,,'''''',,;;;;;;:;;::
#lllllcc:,'..  ....                ... ..',,,,,',,,,,,,,'''........'''',,''..................................'..',,;;,,'',;;;;,,,,,
#llllc:;,'....';,..                    ...',;cc;;,''''''''..........''',,,,'....................'''''..........',;:clc:;'',,''',,,,
#cccc:;,'....'cc:'.                   ....',:occl;...',,,..........'',,,,,,....'''.............................,:lodddol;'.',:ccc:;
#;;;;;,'......;:,. ...,:;'..        ....''',;:ccc;,,',,,'...........''',,,'...,,,'......':cc;'.................;cloxkkxdc;;:lodddoc
#',,,,'.......... .:dOOO0Oxl;.     .....'''',;cllc:;,;,,'''.....'''''''','...',;,'.......,;;;'...','...........;:lxxkkkxocldkOOxdoo
#...''........   .ck000KXXKOo;.    ......'''',,;;;,,,,''''''''''',,,,,,,'...',;;;,'.........'..................';loooooooodxxkkOxlc
#.......,:ccc;'..;dkkxxO0K0xlc,.  .......''',,,''''''''','',,,,,;;;,,,''..',,;;;;;,'......'''''.................,:llllloolooooodoc;
#.';:;:dO000Okdl:cooooolooxdll;.  .......'',,,,,,,,''''''..'''''''''''''',;;;;;;;;,,'......'''''''''''''.....''..,;cclllllllllll:,'
#.';:cx00Okxxddolllllllllcllcc;.  .......'',,,;;;;;;;,,,,,,,,,,,,,,,,,,,,,;;;;;:::;;;,'.......''............',,'..';:ccllllcc:;,'.'
#.';:lxkxxdooollllclcccccccc::,.  .......'',,,;;;;;;;;;;;;:::::::;;;;,,,,,;;;:::ccc::;;,'.''',,,,'''''''.''',,,,'..',;:cc::;,'..',;
#.';::oddooolllllcccccccccc::;..  .......''',,,;;;::::::::::::;;;;;,,',,,;;;:::cccc::;;,,'''',;;;,,,,,,'.''',,,,,'...,,,,,'...',,;;
#.';c::lolllddolcccccccccc::;,.    ........'',,,;;;::::;;;;;;;;;;;,,'',,,,;;;;;;::;;;,'......',;;,,,,'''..''','',,'...'....',,,,,,,
#..,:c:::cccxKKOkxdolcccc::;,'..   .........''',,,;;;;;;;;,,,,,,,;;;,,''...''''',,,,'.........',,,,'''....''','',,,''...'',,,,,,,,,
#'',:llcc::lOXXXK0dc::::::;;'...   ..........''''',,,,,,,,,,,,,,,;;;;;,,''''''.................'''''......''','','''''''''',,,,;;::
#..':cllllok0KKK0d:;;:::;;;,.....  ...............''''''''''',,,,,;;,,,''.................................''''''';cooc;',:ll:,'',;;
#..';ccccllc:ldkkl,,;;;;;;,.. ...   ................''''''''''''''''''.....................................''''',cdxxdc:lxkkx:',;;;
#..',cccccc;..,;c:'..'',,,..        ..................''..............''''''''''''..................... ........':llclccllllo:,;:cc
#.'',:cccllc,.......  .....         ...............................''''''',,''''''...................    ........';:ccccccc::,,;:cl
#.''',:ccccc:..    ..','..            ..............................''''''',,,,,,''''''''............    ....''''.',;:ccc:;,,;;;;:c
#''''';ccccc:'.  .;dO00Oxl,.          ...............................'''',,,,,;;;,,,,,,,,'..........    ..''''''''..',;:;,..,;;'.''
#.'''';::::::;. .ck00OOkkxd:.          ...........................'''''',,,,,,,,,'''''''...........    ...........'...''....',,'...
#....';ldddol:'.;dxxdddooool;.          .........................''''''''''''''...................   ....'''.''''..''.......''''...
#...'ck0K0Okxoc:clolllllcclc;.          ...........................''''''''.................................'..'';cc;'.''''',,,;;;;
#...:xOkxxdooollccccccccccc:;..        .............................................................'..........'cdkkdc;cool;;;;;:::
#...;oddoollllccccccccccc::;,''..........................................................................'''''';coololldk0Ol;;;;:::
#...':llllcccccccccccccc::;,,;;,,'.................................................................''''',,,,,;;cdOkoccclldo:;;;;:::
#....';:cccccccccccccccc::;',;:;;;'............................................................'',,,,,,,;;;;;;;cdkdlccc::::;;;;::::
#......',;;::::ccccccccc:;,';;,''...........................   .....................   .......'',,;;;;;;;;;;;;;;::;;;:;;;;;;;;:::::
#........''',;;;:::cccc:;,..................................      ..  ...                      ..',;;;;;;;;;;;;;;;;,;;;;;:::;;:::::
#.............'',,;;;;;,,....   ............................                                      ..........';;;;;;;;;;;;;;;;;;::::
#.................''',''.....   .............................                                               ..';;;;;;;;;;;;;;;;;:::
#............................    ............................                          .                      ..''..........'',;;;;
#     ......................     ...............................                     ...                                    ...,;;;
#              .............    .....................................           ... ....                                     ...',;
#           ...........     .......................................       ........                                       ....,,
#.......          .........     .......................................       ........                                         ..''

#;;'  .;,,'''.........''.....................................................................................'''',,,;;;;,,,''''....
#;;'...;;,,,'.........''....................................................................................',,;;;::cccc::;,,,'''''
#:;,. .;;,,,'..........''...............................................................................''',,;:ccloddddolcc:;;;,,:l
#,;.  ';,,,''..........''..............................................................................''',,;:cldxO0KK0Okdoc::;:ckN
#c:''',;,,''............'.........'''''''.............'..........................'''''''''..............'',,;cldk0NWMMWNKkdlcc::cd0
#l:,,;;;;,,,............''....'',,,,,'.........'''''.............''''',,,,,,,,''''.......................',;:cldkKWMMMMWXOxoll;;;;;
#;,...,;;,,'............'''';;,,,''....   ........''..';:;;;;;;;;,,,,,'''................................',;;cloxOKNNNNXKkdlc:;,,''
#,'. .;;,,''............';;;;,,,'....          .......':lc;,''...........................................',,;:cclodxkO0kdol:;;,''..
#;'...,;'..............,;;,,,'..........         ......',:c,'............................................'',,;;::ccllodoc::;,''''..
#;'. .',.......''',,,;:c;,''...',,;;,,'.....   ..........',,'';;..........................................',,,,,;;;:::cc;;;,,''....
#;'...',..','''''''',:cc;'';:looddooollc:;,'...............'..;:,..........................................',''',,,,,,;;;;,,'......
#;'. .',........'...,;;;;:oxkkkxxxxxxddddoolc:;,'..........'',;:c;'........................................''''..'''',cc;,..'''....
#,.  .,,..... .,,...,,,,;cloodxxxxxxxxxxxxxdddollc:;,,''..'''',:lol:'................................................,cc,'.........
#,. ..,,''''..,;..,clcldxxoc;;;::cloddxxxxxxxxxxxxddollc:;,,,,,,:oxxc'............';ccc;'.............',,'''........',:;''.........
#,. .';,',,'';;..,cc:lkOkxdlc:;,''',;:loddxxxxxxkkxxxxxxxdollc;;:lodd:...........'lddddxo'..........''',,,''..'..''',::,,'.........
#,. .,;,,;:;;:'.,;;;lkkxdddoollc:;,,,,,;:lodxxxxkkxxxxxxkkkxxxdodddooo:'........'coollloo,...........',,,,,,,,,,,,,,,;,','.........
#,...:cloxkxo;.,,';lkkkxxxddoolllccccc::;;:lodxxxxxxxxxkkkkkkkkkkkkkxxo,.......;llodlllo:...........'',;::::::;;;;,''''',''''''....
#oloxOO000kxc.,;.,okkkkxxdoollllllllllclc:;;;:lodxxxddddxxxxkkkkOOOOkxol,....'lxoxkdlllo;...........';:clooddoolc:;;,,,,;,'''''''..
#00000000kxo:':,,oOkkxdoc:;;;;;::cccccccll:'...;:clolllllclooxkOO00OOklcc'...cO0Okooollo:..........';:coxkOKK0Okxdoccc::cc:,',''''.
#0000OOOkxdoc,,;lkkkxxddol:;,'',,',;:cccc:'.......,:cc:::;;;:clxO000kkl:l,...cO0xlclool;........'',;:cldk0NWMWWX0kdoccc:clo:'''''''
#0OOkkxddoooc;:lloodddddollcc:::;;;;:cc:'',:loc,..,lllllllccc:::lxOOOklldc...,odolcllc;''',,,'''',,;;clox0XWMMMWKOxdoc;;:cc;'''....
#kkxxxdoooooccdkxdocccccllllllccccccc;'':ldxkkx:..:lllloooddddolllooddlldo;',lxoodc,'''''.......''',;:cloxk0KXXK0kxdlc;;:l:,,,'....
#dxxxddooool:cxkkkxxdolccc:::ccccc:;'':oxxxkkkx:..cllcclloooddddxxdxdlc:lo;'ckkxxx:............'''',,;;:cloddxxkKKkdol:;;cc',;''''.
#:odddddoooc:lxkkkkxxxxdddoolc:::::;:oxxxxkkkkx:..clc:::::cloodxxxxkkddl;;';dOkkkxc..........''''''',,,;;:ccllodO00K0kxdllc,,;'....
#.,coddoool:;oxxxxxxdddddoooooooddodxxxxxxkkkkxc..colc::;;;::ldxxxxkxodol;.,dxdddo;...........''''''',,,,;;;::cclx0NNN0dcll;;,''''.
#..';cooooc;;lddddddoooooooooooodddxxxxxxkkkkkxl,.cdoollclccccldxxxkdlolc,.;kkdlc:''''.'......''''''''',,,,,;;;;::lxOkdoc::,''''...
#....';lol:,;loooooooodddddoooooddxxxdddxxkkkkxol:;oxxxdoloodoooxkkklcc;,.;kOkxo;'''''''''''''''''''''''',,,,,,,,,,;;;:::,'''......
#......,cc;,;clloooooddddddolloddddddoddddxkkkxdoollodxkkdddddxxxkkd;,::,cxkxdxx:'''''''''''''''''''''''''''''''''''''';;,'........
#.......';,,:cllllloooooooolloolcccllloooddxkkxxddddoooddddxxkkkOkkl'co;cOOxdooo:''''''''''''''''''''''''''............';'.........
#.........',:ccllllloooooolcccc:,..;ccllooddxkxddddoddddddoodddxkkdlcl:lk000kdlc;''''''.................................,'.........
#.........',::ccccllloooolc:::::,..;ccllc::cdxxdddddddddxxkkxdddxdolcclxO0KKkkx:''......................................''...'''',,
#.........',;:::ccclllooolcc::c::;:ccclc,',:lddddddddddddxxkkkOOOkxoloxkOO00kOO:.............................'''',,,,;;;;;;;;;;;,,,
#.........',,,;;;::cclllllllllllllllclllc::clodddddddxxdddxxkkOOOxoodxkOOOOO0KOc..............'''',,,,;;;;:::::::::;;;;;,,,,,''''''
#.........',,''',,;:ccclllllllllllllllloooolooddddddddddddxxkkOOxoodxxkOO00O000l''',,,,;;;;:::::::::::;;;;,,,,,,,''''''''..........
#..  ..  .,'....'',,;;;:::::::cclllllooddxxxxxxddddddddddddxxkkxddxxxkkkO000O0Oo::::::::;;;;;,,,,''''''............................
#   .',............''''',,,,;;cclloodxxxxxxxxddddooddddxxxdodxxxkkkkOO00O0kc,,,''...................          .................
#..    .';,......   ......',;cc:;,;;;;:clodxxxxxxddddoodddxxdoodxxxxxkkkOO00O0k;......              ...............''''''',,,,;;;;;
#     .',,'.....          ..;cooccll:,',;:codxxxdooooooddddolodxxxxxxxkkkO00O0k,      .............''',,,,,;;;;;;:::::::::ccccccccc
#    .',,,'..................'''',;:,'....',:lddocclooooddolodddddddollodkOOkOkc,'.''',,,,;;;;;;;:::::cccccccllllllllllllllllllclcc
#   ..',,'.........''',,,,,,,'','....... .....;cc::cloooolcloool:;;,'',,;cllodxkxoc:::::cccccccclllllllllllllllllllllllccccccc:::::
#   ..,,'..........''''',;;::::::;;;,'..     ..;:::cllllc::c:,'........'',;,;:codxxdocllllllllllllllllllllllcccccccc:::::::::::;;;,
#.....,,'...............'',,;;::::cccc:;'....',;::cclcc:,'...................';cccldddllccccccc::::::::::::::::::::;;;,,,'''.......
#:c'..','.............'',,,,;;;,,,;;;:::;,,,;;:::cccc:;..   ........     ....';coooooddo:;;;,'......''''''''''.....................
#od;...'''...........',,;;::::::;;,,,,,,,,,,;::::cc:;'.      ...       .....',;:lodxxxkkxdoc,...........         ..................
#lxo,...'''''''''..'',,;;::::::::;;;;;,,,,,;;:::::;,..               ........',;;:clodxxxkkOxo;.        ..............'',,,;;;:::::
#okkl,...''''''''''',,,,;::::::::::;;;;;;;;;:::::;'..                  .......',,;;:ccooddxxxxxdc,..........',,,;;:cclllllllccc:;;,
#oxkd:'..'''',,,,'''',,,,;:;;;;;;::c:::::::::cc:;'.                     .........',,;;::clloddxxxdoc;;;;::::clllccccc::::;;;;;;,,,'
#dxxoc;'..''',,;,'..'''',,,;;;;,;;:ccc:::ccccc:,..                       .........',,,,;;;::ccoodxxxxdl:;;;,,;;,,,,,,;;;;;;;;,,,''.
#xdolc:,....'',;;,'''..'',,;;;;;::ccc::cccccc;'...                        .........',,;;,,,,;;;;cldkO0kdlc;;,,,,,,;;;;;;;;,,,'''''.

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWN0xxO0XNWWNNNXKKKXXXNNNNWWNNNNNNNWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNOc'.,cok0K00OxoclokOOOO00000000000KKKK0XNWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWXx,..:dxxxxdolllc::codddddxkkO000OOOO0Od::d0NWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMWWWWWWWNNKOl'..cxkxdl;''''',,,,;clolllodxO0000Okkxl;',cdOXWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMWWWWNK0kdol:,..:dxdo:'.......''..',:cclloddkOOOkxdlc,.....:xXWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMWWNX0kdlc:;;;;;'.,ldol;....;:'..;c,..',;coxkkkkkkkkxol:,......,xXWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMWN0kdc:;;,'''',,,..:llc;'....,,..'cd:'',;:codxkO0OOO00OOkxdlc:;,,l0NWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMXkl;,,,,,'...''',,.'ccclc;;,'''''.',,',,;;:llodxkO0KKXXXKK0OOOOkkxxxO0KXXNNWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMM0c,''',,,,'...'','',:coooolc:,,''....,;::ccllodxOKXXXXXK0kxddddolc:;;,;;:cokKNWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMXo,''',;;;,'..''',,;:codoollllc:;,,;:cccllllodx0KXKKK0Oxoccooc::;,,,,'......;kNWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMW0l;,,;:::;'...',,;:coxkxdolloolllloooolooooxOKXXXK0Oxl;'',,,,,'..  .........,xNWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMWKd:;;:cc:;'..',,;cldkOOkxdoodxxxxxxddoddxOKXNNXK0Okd:'........     .........lXWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMNOo::::::,..';;;cok000OkkkOOOOkkkxxdddk0XNNNXKK0Okd:'.''..       ........ .dXWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMWXkl::::;'.,;:codO0KK0000000OOOkxxdxkKXNXXKK00Okkdc,'';;'.....'''... ....lXWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMWXkl:;;,,;clodxk0KKKK0OkkkOO00000KXXXXXK00OOOOkdl;'..',,;;,,,'..   .''.c0XNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMWXOdoc:;;cloodxkOKK00koccdO0KXXXXXXXXXXK00Okkkxdl:,'........      ....':lldkOKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMWNOxooooolllooodxxkOOOOdc;;cd0KXXXXXXXKK000Okxxxxdlc:,'.....        ...,cccccccloxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMWKxdooooooooooooodxxxxxkxl;,,:ok0KKKKKKK00Okkxdlllc:;,.........     ...,clcccccccccccoxOKNWMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMXOdooooooooooooooodxddddxxdl;,',:ok0KKKKKK000kkxolc:,'............ ...',:llccccccccccccccldkKNWMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMWKkdooooooooooooooooooddodoooddlc::cldO0KKKKKK0Okkdool:;,''''''',,'...',;:colccccccccccccccccccokKNWMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMWKxdddoooooooooooooooolddddooodxxdodddxk0000OOOkkxdoolllc:;;;;,,,,...';:::cllcccccccccccccccccccccldOXWMMMMMMMMMMMMMM
#MMMMMMMMMMMMW0xddddoooooooooooooodoloxkxxddxkkkkxxkkOKKK0Oxddoc;,,,,''.............':loolcccccccccccccccccccccccccokXWMMMMMMMMMMMM
#MMMMMMMMMMMW0xddddddoooooooooooooooloxkkkkxkkkkOOOOO0KKKKK0OOOxl:::,''...........',:clllccccccccccccccccccccccccccccokXWMMMMMMMMMM
#MMMMMMMMMMW0xdddddddoooooooooooooooodxkkOOkkkOO00K0000KKKKKK000Okkxdolllc::;;:::clllcccccccccccccccccccccccccccccccccco0NMMMMMMMMM
#MMMMMMMMMWKxddddddddoooooooooooooooodxkOO00O00KKKKKKK00O0000000000OOkkOkxxxxkkxdollcccccccccccccccccccccccccccccccccccclkXWMMMMMMM
#MMMMMMMMMXkddddddddooooooooooooooooodxxO0KKKKXXXXXXXK0OOOOOOO0000K0000kxxkOOkxolccccccccccccccccccccccccccccccccccccc:::cxXWMMMMMM
#MMMMMMMMNOddddddddddooooooooooooooodxxxOXXXNNNNNXXXK0OkOOOOOO0KK0000KOdccokkolcccccccccccccccccccccccccccccccccccccccc:::cdXWMMMMM
#MMMMMMMWKxdddddddddooodooooooooooooxkkk0XNNNNNNXXXXKOOOOOOO00KKK0000KKkl:lxkdlccccccccccccccccccccccccccccccccccccccccc:c:cxNMMMMM
#MMMMMMMNkddddddddddoddooooooooooodxkkkOKNNNNNNXXXXK00000O000KK000000KK0xllxOkdlccccccccccccccccccccccccccccccccccccccccc:::lOWMMMM
#MMMMMMWKxddddddddddddooooooooooodxxxxO0XNNNNXXXXXKKKK00000KK00000000KKK0xdxdxxoccccccccccccccccccccccccccccccccccccccccc::::dXMMMM
#MMMMMMNOddddddddddddddoooooooooxkkkkk0XNNNNNXXXXKKKKKK000KK00000000000KKkkxoxkdlcccccccccccccccccccccccccccccccccccccccc:cc:lOWMMM
#MMMMMWKxddddddddddddddooooooooxxxkOOOKXNNNNNXXXKKKKK000000000KKKKKK000KKOdddkkxlccccccccccccccccccccccccccccccccccccccccc::cckNMMM
#MMMMMW0dddddddddddddddoodoooodkkxxkO0KXNNNNNNXXXKKK00000KKKKKKKKKKK00KKK0xddkkdolccccccccccccccccccccccccccccccccccccccccc:ccxNMMM
#MMMMMNOddddddddddddddddodooooxkkddxO0KXXXNNNXXXXXKKKKKKKKKKKXXXXKK000KKK0kddxdollcccccllllcccccccccccccccccccccccccccccccc:ccxNMMM
#MMMMMXkdddddddddddddddddoooooxOkxxkO0KKXXXXXXXXXKKKKKKKKKKKXXXXXKK0000KKKOxdolccclcllclllllcccccccccccccccccccccccccccccccccckWMMM
#MMMMMXkddddddddddddddddddddooxOOO0KKXXXXXXXXXXKKKKKK00000KXXXXXXKK0O0KKKKOxdolcccllllllllllcccccccccccccccccccccccccccccccc:l0WMMM
#MMMMMKxdddddddddddddddddddddox0KKKXXXXXXXXXKKKKK00000000KKXXXKKK00000KKKK0kxolcclllllllllllccccccccccccccccccccccccccccccc:cxXMMMM
#MMMMMKxdddddddddddddddddddddod0XXXXXXXXXXXKKKK00000000KKKXKKKK000000KKKKK00kocccllllllllllllccccccccccccccccccccccccccccccclOWMMMM
#MMMMMKxddddddddddddddddddoddodOXXXXKKKKKKKKK00000000KKXXXKKK0000KKKKKKKKKK0xllllllllllllllllcccccccccccccccccccccccccccccccxNMMMMM
#MMMMMXkdddddddddddddddddddoooodOXXXXKKKKK000KKKKKKKKXXXXK00000KKKKKKKKKKXX0dlclllllllllllllllcccccccccccccccccccccccccccccdKWMMMMM
#MMMMMNkdddddddddddddddddddodooodkKXXKKKKKKKKXXKKKKKKKKKK0000KKKKKKKKKKKXXKkolllllllllllllllllcccccccccccccccccccccccccccco0WMMMMMM
#MMMMMW0ddddddddddddddddddddoooooddk0KKXXXXXXXNXXXKKKKKK0KKKKKKKKKKKKXXKXX0dllllllllllllllllllccccccccccccccccccccccccccclOWMMMMMMM
#MMMMMWKxddddddddddddddddddddooooooodxkO000KKXXNXXXKKKKKKXKKKKKKKXXXXXKKK0xllllllllllllllllllllcccccccccccccccccccccccccoOWMMMMMMMM
#MMMMMMNOddddddddddddddddddddoodoooooooodxO000KXXXKKKKKKKKKKKKKXKKKKKKKKKkollllllllllllllllllllllcccccccccccccccccccccco0WMMMMMMMMM
#MMMMMMWKxddddddddddddddddddddoddooooooooxO0000KK000K0OOkkkkO0KKKKKKKKKKKkollllllllllllllllllllllccccccccccccccccccccco0WMMMMMMMMMM
#MMMMMMMNOdddddddddddddddddddddodooooooox0KK000K0Okkkxdoooooodk000KKKKKXXOolllllllllllllllllllllcccccccccccccccccccccdKWMMMMMMMMMMM
#MMMMMMMWXkddddddddddddddddddddoooooooodOXXXXKKK0kdoollooooooldO000KKKXXXkollllllllllllllllllllllcccccccccccccccccclkXWMMMMMMMMMMMM
#MMMMMMMMWKxddddddddddddddddddddoodooodk0XXXXXXKOdoooooooooooodO0KKKKXXXKxlllllllllllllllllllllllcccccccccccccccccoONMMMMMMMMMMMMMM
#MMMMMMMMMW0xddddddddddddddddddddddooodk0KK000Okdooooooooooooox00KKKKXXXKxllllllllllllllllllllllllccccccccccccccldKWMMMMMMMMMMMMMMM
#MMMMMMMMMMW0xddddddddddddddddddodooooodxkxxdddoooooooooooooook0KKKK0KKXKxllllllllllllllllllllllllccccccccccccclkXMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMW0xdddddddddddddddddddooooooooooooooooooooooooooook0K00000KKKkollllllllllllllllllllllllccccccccccld0WMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMWKxdddddddddddddddddoddooooooooooooooooooooooooook000000KKKKOdlllllllllllllllllllllllllcccccccclkXWMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMWXkdddddddddddddddddodoooooooooooooooooooooooooox0K00KKKXXXKkollllllllllllllllllllllllccccccld0WMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMWNOxddddddddddddddddooooooooooooooooooooooooooox0KKKXXXXKKKOollllllllllllllllllllllllcclccokXWMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMWKkddddddddddddddddddoooooooooooooooooooooooodk0KKKKKK0OOxollllllllllllllllllllllllllclxKWMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMWNOxdddddddddddddddoooooooooooooooooooooooooodxkO000K0Odollllllllllllllllllllllllllld0NMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMWXOxdddddddddddddoooooooooooooooooooooooooooooddkkOOxolllllllllllllllllllllllllldOXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMNKkdddddddddddddddooooooooooooooooooooooooooooodddollllllllllllllllllllllllldOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMNKOdddddddddddddoooooooooooooooooooooooooooooooollllllllllllllllllllllloxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMWXOxdddddddddddoooooooooooooooooooooooooooooooollllllllllllllllllllokKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kxdddddddddoooooooooooooooooooooooooooooollllllllllllllllllox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0Oxddddoodoooooooooooooooooooooooooooooooolllllllllllldk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0kxddoooooooooooooooooooooooooooooooollllllllodxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0Okxddooooooooooooooooooooooooooooloodxk0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKK0OOkkxxdddddooddddddddxxkOO0KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNXXXXXXXXXXXXNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

#llooooooooooooooooooooodddoddddddddddoollllccoddddddddddddddddddddxxxxdddxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkkkxkkkkkk
#lxxddddddddddxxxxxxxxdodxxddddddddxxdoollollodxxxddxxkkkkkkkxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkOkkkkkkOOOkOOOOOOOOOOOOOO0O
#lxxlllllllllllllooooc;:cccc::::::llolc:::cllcccccccloddddddddddddddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxk00
#lxxllllllllllooooooc;;;;:ll;'.''',:c:;,,,',;c:::clc:coddxdddddddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkk00
#lxdcccclllllllllll:,,,;;:;'.....',;::;:ll:;,;:::ccccc::clooooooddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkk00
#lxdcccccccllllll:,,;;;:;'....',;ccc:::coddlc:;:clolc:;'..';:coooooooddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkk00
#lxxlllllllllool;...::'......',:lll:;:;;cloolc;;;;:cc;;,'....,codddoolooddddddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkO0
#oxxlllloooool:'...,;,......''';odoc::::::::,,:c;,'',,,,,,...';;clodxdoodddddddddxxxxxxxdddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkO0
#oxxllloooooo:'..,;,,,,'..',,'':llc:;;;;;;;,'..':::;,,'...';;;;,,;:cdxxdodddxxdxxxxxxxxxdddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkxxxkxk00
#oxxllloooool,..';cclooc;;:,',::cccc:ccc:;:;'...,:;;;;;'............,:odooodxxdxxxxxxxxxdddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkk00
#lxxllllllll;. .,cdkOOkdolc:;::clllcllc:::::'....,;;:;::;'.......''...,:llldxxxxxxxxxxxxddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkk00
#lxxlllllllc'  .:dOO0OOkxxdolllodooooollcc:;,,,;:::c::::cc;,'....','''',:lccdxdxddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxk00
#oxxloooolc,. ..cxO0OOkkkkkxxxkkxxdxxxxddddolllloooool::c::cc:;;,;,,,,;;;lollddxxxxddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxOO
#okxoooool,.  .'lkOOOkddkOOOOOOOOOOOOOOOkkkkkkkkxxxxxo::cccc:cc:,,,,',;;,;:lllodxxxxxxxxxxxxxxxxdddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxk00
#oxxooool;.   .,cxOOkxxxkOO00000OOO00000OOOOOOOOkkxxxo:lolodlc::,'''''','',,,;ccldxxxxxxxxxxxxxxxddxxxxxxxxxxxxxxxxxxxxxxxxxkkkxk00
#oxxoool:'.  .';cdkkxxkkkkOOOO00OO0000OOOOOOOOOkkkkkxo;:olloddlc,''',,,''',,,;:ccoddxxxxxxxxxxxxxddxxxxxxxxxxxxxxxxxxxxxxxxxkkkxk00
#okxooc;:,.  .,codxdodxxxkkOOOOOOOOOOOOOOOOOOOkkxkkkxdc;lol:cccc;,,,'..',,,'',,;:clodddddddddxxxdddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxk00
#okxol;,,..  .:loddolooodxkkkOOkkkkOOOOOOOkkkkkkxkkkxdo::ldxoc::;,'...........';:c:cldddddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxk0O
#okxol;'.'.  .:ooolllcc:clodxkkkkkkkkkkkkkkkkxxxxxkkxooolclddlllc,'............;cl::ldddddddddddddddddddxxxxxxxxxxxxxxxxxxxxxxxxxOO
#okxooc'.'.  .cooolcc:;;;;coxxxkkkkkkkkkkkkkkkkxxkkkdooollllllcc:,......  .....',:coxxxddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxOO
#okxolc,..   .:lllcc:;,'.';ldxkkkkkkkkkkkkkOOOkkkkkxddoolllloollc,'..........,;,,'';oxxdddddddddddddxxxxxxxxxxxxxxxxxxxxxxdxxxxxxOO
#oxxlc;,'.....,:clc:;,'..';:oxkkkxxxxxkkkkOOOOOkxxddoollclllooool:;'.........,;::;'':dxdddddddddddddddddddddddxxxxxxxxxxxdddxxxxxOO
#okd:,.''''....,:cc;''...',;codxkkkkkkxxkkkkkkxollc::;;,',;:cloooc:,.  ......',;::;,;odddddddddddddddddddddddddddddddxxxxdddxxxxxOO
#oxl,'''.,;'....,:c;'....'',;ccloxxdxkxxxdddoc:,'......  ..,;:looc::,..........,;:;,,cddddddddddddddddddddddddddddddddddddddddddxOO
#odl;;;,.''......;c:'..........';:ccloolc:;'..            ..,:ccllcc;..  .......';,,:lddddddddddddddddddddddddddddddddddddddddddxOO
#oxd:;;'.     ...,::'..          ...,:c:,.          .      .,loolcc:,............'';loodddddddddddddddddddddddddddddddddddddddddxOO
#ldo;;,..      ..';:,..              'col;.     ......  ..,cdxxdollc;'.............,loddddddddddddddddddddddddddddddddddddddddddxOO
#ldl,'''..   .....,;;'.       ...   .:dkkdc,...........';codxxddolccc;'',,'.  ..'..;loodddddddddddddddddddddddddddddddddddddddddxOO
#lxo;'.''.....'...':c;'.      ......,okOOkxollc:;,,,,;:lodxxddolc:;:c:,,,,..  ..'.':looooooooooooooooooodddddddddddddddddddddddddOk
#oxxl:'...,'. ..  .;cc:,..     ...':ldxkOkxxxdddolllloooooollccc::::c;,,;;.    ..':loooooooolllloooooooooooooooooooooooooooooooodkk
#lxxllc;..;;..    .':c::;,'....',;:loddkkkxxxddoollodxxxdddoc::;,;:c:;,''..    ...,:looooooooooooooooooooooooooooooooooooooooooodkk
#lxdlllc:;;,.. .. ..,:cllc:::::;coollodxkkkxxdoccclodxxxxdddolc:''';;;,.  .    ...',:loooooooooooooooooooooooooooooooooooooooooodkk
#cddcccc:::'...''.. .,,;:cc:cooccolccldxxxxxxddolcloddddxdddddoc,..';;,.   .   ....,;clloooooooooooooooooooooooooooooooooooooooodkk
#cddccccc:;'.',,;.   ...,cccoddolllcloddddddollolllolllloooooc:;,'.';:;,....   .':,;::cllllllooooooooooooooooooooooooooooooooooookk
#lxdcccc:;,,;;;,,..  ..'';clooddooolc::cccc;....,cddoolc::;;;'......,;,.....   .':;:lllllllllllllllllllllllllllllllllooooolloooookk
#lddcccc:::ccccc:'.. ....,:loddooddo;..........,coddooool:,... .....','......  .;:cllllllllllllllllllllllllllllllllllllllllllllloxx
#cddccccc:ccccccc;,,'.....,:loooodddl;,'....';cooolc:,,,''.........';,'.''... .:clllllllllllllllllllllllllllllllllllllllllllllllokx
#cdo::::::::cccccc:;;;'....,::coddddolc:;,,,;:cllc;,.     .......',,,.',,,'..':ccllllllllllllllllllllllllllllllllllllllllllllllloxx
#:do::::::::::::::::;::;'...',:clccc:;,'...........       ......',,'..;cc:;,:clllllllllllllllllllllllllllllllllllllllllllllllllloxx
#cdo:::::::::::::::::c:::'..........   ..................  ....''.....;cccccccccccccccccccccccccccccccccccccclllcccllllllllllllllxx
#cdo::::::::::::::::ccccc:,...       ...............',,'......''.......,cllccccccccccccccccccccccccccccccccccccccccccccccccccccclxd
#:do::::::::::::::::::cccc:,....   .............',;:cc:;'.............  ,ccccccccccccccccccccccccccccccccccccccccccccccccccccccccdd
#:oo:::::::::::::;:::::ccc;.  .......'''',,,;;::cllllcc:'............   .:cccccccccccccccccccccccccccccccccccccccccccccccccccccclxd
#:oo;;;;;;;;;;;;;;;;::::::'    .....';::::cclllooooolc:,..........     ..,:ccccccccccc::::cccccccccccccccccccccccccccccccccccccclxd
#:ol;;;;;;;;;;;;;;;;:;:;;,..     ....,;ccc:cclllllc:;,....            ....,::::::::::::::::::::::::::::::::::::cccccccccc::ccccccdd
#:oo;;;;;;;;;;;;;::::;,.. ...        ..,;;;;;;::;;,'..                .. .......',;;::::::::::::::::::::::::::::::::::::::::::::cdd
#:oo;;;;;;;;;;;;;:;;'.     ....         ............           ...       ........ .',;;:::::::::::;::::::::::::::::::::::::::::::dd
#;ol;;;;;;;;;;;;;,..      ......                              ........   ............'',;::::::::::::::::::::::::::::::::::::::::do
#;ol;,,,;;;;,,,'..       ......   ..                         ...........................',,;;;;;;;;;;;;;;;;:::;;;;;;:::::::::::::do
#;ol,,,,,''......    .   .............                      ..........  ......'.........''''';:;;;;::;;::::::;:;;;;;;;;;;;;;;;;;:oo
#;ol,''..........  ..ll.'ol:xxloxd:..;xdo;'cddc,cdl;lxo;cdcll:oodkkd;..:xxllxkklckxldxclkxc''okxkxxddxdk0kdkdlko;;;;;;;;;;;;;;;;:oo
#,lc................'k0,,0xdX0lxNO;  lKdk0kKooKxOXdckKkckWXXk;,'oXNd..;0O::O0o0OxXNKXNxkNk;..dXNNNKxO0lxXxlKK0Nx;,;;;;;;;;;;;;;;;oo
#.c:.................xXol0xoKd,dX0:  lKOOxoOkkOoOXx:l0Xkk0ONk'..cKXo..,kKdck0k0xx0KNKKxkNOc..oNX0NKok0cdKolK0kXx,,,,,,,,,,,,,,,,;ol
#.c:.................;cc;:;;c'.,:c,  'cc;..'::..,:;,,:c,;;,:;...,cc,...;ll;;cl:',::c:c::cc:'';ll:cc;:c,:l::lc:oc,,,,,,,,,,,,,,,,;ol
#.c:.......   ......,dxc..'oo:oc:do;cdo:cddl.  :x::d:.:kd,:xlllcdc'co;:kx;;d:...'lolxko,.,dkdldkkl:dxlokllkxodkxl;,,,,,,,,,,,,,,;ll
#.::................oKXO;.;0Oo0xdKOcxXOlkXXK: .kWKKWx:kXKodNXXOxKd;x0okXXxoKo...,OO:xKl..oKd;xKdk0xKWKXNkkNOoxK0l,,,,,,,,,,,,,,,,ll
#.::...............'k0OKl.,k0O0l:kXkkXOokKK0; .xKKKKkx0OKkx0OXOo00x0Od000OxKk:;::kk,d0;..l0kld0kOOd0KXXKxkX0ooOXk;',,,,'''''',,',ll
#.:;................;,':,...;:,.,:;',cc,,,',.  ';::::::,;;,;,:;';llc,,:,,:;cc;;:,;;.,:...';lc;;cc,,::::;,;ll::ll;''''''''''''''',ll
#.:;....................     .... ...'lloolc:lclkxldl:dc..,dOl'..lkkllkl;oxxlcxkold::ocdkoldkxl'..................'...''...''''',lc
#.:;..................     ...... ...'kXNNXxo0lcKk:OKOXd..lKXO;.'kWWKKWkx0ox0lxKllK000x0XooKXXx'...............................''cc
#.:;..... ...........    ........... .xN00Ndl0c:0d;k0x0d.'x0O0l.'kX0KKKkoOkOk,o0:c0xk0d0Kdd0KKd..................................cc
#.:;.....  ... ......  ............. ..,'':'',..,'.,,';'..,,','..,;,;,,,.,::'.';..,',;,;c;,;,,,..................................cc
#.:;.....      . .... ..............     ........   ..........................   ................... ....................   .....::
#.;;......         ..  ........  ...    ..................................     ....................  ....................  ......::
#.;;......                ....  ......   ..............................     ........... ..  .  ...   ..... ......................::
#.;;.......               .... .......     ..     ..................     .........             ..    ..   ....  .........  ......;;
#.;;.   ...                .        ...        ........       ..       .......                 .    ....  ...   .........  ......;;
#.;,                                ...      .                       ..                            ..........  .........   ......;,
#.;,                                                                                                ..  ...    .......     ....  ;,
#.;,                                                                                                .         .      .     ..   .;;
#.;,                                                                                                                            .;;
#.;,                                                                                              ..                            .;;
#.;,                                                                                                                            .;,
#.;,                                                                                                    ..                       ;,
# ;,                                                                                                    .                        ;,
# ,,                                                                                                                             ,,
# ,,                                                                                                                             ,,
# ,,                                                                                                                             ,,
# ,,                          .  ... .. ..  .. ...  '.  ..  .'. ..  .. .'..........    .. ..  .. '. ...                          ,,
# ,'                             ... ..     .. ...  .. ...  .'. ..  .. ............    .. .. ... .. ..                           ,,
# ';'.....''''''''''......................................'''..''''.................''.............................'''.........'';'
#  ............................................................................................................................... 


#....                                                                                                                              
#.............................                                                                                                     
#.............................                                                                                                     
#................................                                        ......                                                    
#......................................                       ....',,;;;::ccccccclc;,.....                                         
#.............................................           ...',;::::::clcc:::::cloxkkkxoc,...                                       
#................................................. .. ...',;,,''''''''''',;,'....';lxO00ko:'..                                     
#.....................................................',,,,,'''..'''....,oxc,;'....'cxKNXKOo;...                                   
#..........................................,;,',;;,'',,,,,;,,,'.';:,.   .:o:.,:,. ...,oXWWWXx;...                                  
#..........................................,;,'''..''',,;;::;;,...,;,.    ..  .'... ..:kKKXN0:...                                  
#.....................................       .....',,;;,;;;::::;,....................',:lldkl...                                   
#....................................       .....''',,,,,,,,,,,,;;;;;,,'.............''',,,,.                                      
#...................................       .....';;,,,,'........'',,;:cc:;,'...'',,;;,'......                                      
#...................................      .......,cccdxl'...........'',;,,;;;,'',;::cc:,'..          ............                  
#................................  ..     ...........';c'.................''''''',,''...'.        ..,:cooollooolc:,.........       
#.................'',;;;;,''....    .      ................................''...,;;,,,'...       ....',co:...';ldxxdolllooc;..     
#.....,;;;::::;,;:cccllldkxc'''..         .....   ..............................'''',,,,.       ..............,:lodxxdc'':cc;.     
#....,c;...,coc;coo:,''';oxc.'''..        .....                   ..................''''..     ..........'',;:clllodddo:..,:c,.    
#'..';:.   .;:..;lddddddddl:,,,,,'.............                   .......................      .'''...'''',,,,,;;;cllcc:,';clc.    
#'''',,,'...'...',;:cloddddlll;,,,,;,,;;,'....                            .......................',,,,,''.........'',;cc,,;,'.     
#''''''''''........',,;;;:::cl:;;;;:;;::::,...                         ............................''..'...........',;:;....       
#,,,,,,,,,,,,,,'..',:::;;c:::::::::cccccccc,......                          .......''''''..........'..............'';:,....        
#;;;;;;;:::::;''';;:coc,:lloolllllllc;,''''......,;:;;;,''...            ..,:cccc::::;;;;;;;;;;,,,;:'..      ..';:cc:;:,'..........
#,,,,,,,,,,,,'.,;clccllllllooooooolc;,''''.......,oOKKKK0Okdc.         ..;d0XXOxdooolllllllllloooc;........   ..''.',cddc;;,,,,,,,,
#:::::;;::;;;::ccclllllcclloooddl:,'.......... ..,:coodkOOxl,.          .;loxkxxdollllcccccc::::::;'.........,:lododxkOkl;;;;;;;;;;
#ddddddddddddddddddddddxxddxddo:;;:::c;cc,,'..........,:c,.         ......'',:cloodxxxxxdddoooollllccccc::;;;;,,;;:cllolc::::::::::
#ddddddddddooooooooolllooooool,..,,:llcoo;:xl'.......';,'.      ........,;,'..',,ckKKKKK0Okkxkxxxxxxxxxxxxddddddddoooooooolllllllll
#oollllllccccc::::::::::::::odc;;:,,:lll:;lkOo:'......,;'.      .........'......,okkkkkkkxdlldxxxxxxxxxxxxdddddddddddddddoooooooooo
#llllccccccc::::::;;;;;;;;;,;clddxdoolc::ccc:::,.''..',cooc;.............. .....';;;;:::cccccoddddddddddddddddddddddddddddddddooooo
#ollllllcccc::::;;;;;,,,,,,,''',;:odxxdlc:;',',,.,ldkOKNWWWN0xoc;,'''''''''....'''''',,,,,,,;clooooddddddddddddddddddddddoooooooooo
#oolllllllccccc::::;;;,,,''.....  ..;ldxkkxl::;,';clllodxxk0KKXK0Okdc:ccccccccccccccccccccllloooooooooooooooooooooooooooooooooooooo
#dooooooollllllcccccc:::;;,''.....    ..,:loxkxxdollc::;;,,,;;::::::,;ccccclllllllllllllllooooooooooooooooooooooooooooooooooooooooo
#ddddddoooooooooolllllllcccc:;;,'.....      ..',;;:ccllllllllcccccc::cccclllllllloooooooooooooooooooooooooooooooooooooooooooooooooo
#xdddddddddddddddddoooooooolllllc::;;,''......         ........'',,,;:clllloooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#xxxxxxxxxxxxxxxxxxdddddddddddddoooooollllccc:::;;;;;;;;;;;;::ccclllooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddddddddddddoooooooooooooooooooooooooooodddoodddddddddddddddddddddddddddddddoooooooooooooooooooodoo
#ddddddddddddddddddddoooooooooooooooooooollllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWM
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWNWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#NK00NMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#KOOO0NMMWWWWWWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#XOOOOKNMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#WXOkOOKWMMMWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWXOOOOKWMMWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MMWXOkOOKWMMWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXKKKK000000000OOOk0XNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MMWNKOOO0XWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNX0kdoooddddddddxxkkxxxdxxkOKNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MMWWNKOOk0XWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWN0dlcc:ccccccccllodxkOOO00kxoodxOKNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MMWWWN0OkO0XWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXOo:;,,,'''...'''''',,;;:ccodxkkdoodk0NWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWMWN0OOO0NMMWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWW0o;,,,'',coolclcclodkOOkxxdl:,';lddllooxKNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWMMMWN0kkO0NMMMWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMWk:'.......,''...,:dOKNWMWWWWNKx:,.';::cllokKWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MMWWWWMWXOOOOKNMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWMWk,.,:ldx;.     ..,ckWMMWMMMWWNNXk:,'..,;cclloONWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MMWWWWWWWXOkkOKWMMMMWWWWWWWWWWWWWWWWWWWWWWWWWW0:,oKNNKo.   .  ..'ckWWWWWMMWWNNNNx,....,;:clllxXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWXOkkOKWMMMWMWWWWWWWWWWWWWWWWWWMWWWWXl;kNNNXo.  .......,lONNWWWWWWWNN0xo:,,..',;cccccxNWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWMWKOkkOKWMMWWWWWWWWWWWWWWWWWWWWWMWWWO:dNNNXx,.   .   ..':xXXXXNNWWNOollc;;,'..',:ccc:cOWMWWWMMWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWMWWKOkkOXWMMWWWWWWWWWWWWWWWWWWWWMWWNdcONNNO:. .      ...,lO0000KXKocol'..'....',;:::c:oKWWWWMMWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWMMWWNKkkkOXWMMWWWWWWWWWWWWWWWWWWWWWWKllOKNXd.          ...;ooodxxdclo;.. ......,;,;;;:;:kWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWMMWWWMN0kkkOXWMWWWWWWWWWWWWWWWWWMWWWW0:lOOK0l. ...  ........,;,;;:cl:'..  .. ...:c;:ccc:;oXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWMWWMWN0kkk0XMMWWWWWWWWWWWWWWWWWWWMNk;l0kdoc,'.........'',,;;;;:::,.........'.:o;,:ccccccokKNWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWMWWWWWNOkkk0NWMMMWWWWWWWWWWWWWWWMW0o:c0K0x:''.............'''.....''......''cxc';:cccc:::cldKWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWMMWWWMWXOkkO0NMMMMWWWWWWWWWWWWWWMNxoc;xKOo:,'....................''''.....;ld:',:ccccc:;:c;.,xNWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWXOxkk0NMMWWWWWWWWWWWWWWWWXdll;:l:::,'........................',;clc:.';cclcccc::;,'. ;KMWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWKkxkk0NMWWMWWMWWWWWWWWWWKl:odc:;;;,''......'',,,,;;;;:ccccc::::;'.';clllooollc:,,.. ,0MWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWKkxkOKWMMMWWWWWWWWWWWWWOc;,cddolc:,'''.''',;::ccccloolc:;,''',;:clloooooolllc:,'.. .OMWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWMWWMWKkxdx0NWNWWWWWWWWWWWWWKo;,;:oxxdl;'.....'',;:::cllc;,,;;::cllooooodoooollcccc;,'. .xWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWMWWWWXxccloookNWWWWWWWWWWWWKdccllkKOxl;'......',:cclolc::ccccclllooddxxxdoollcccc:::,. .dWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWMNxc;:llckNWWWWWWWWWMWWKdllloxkd:'.........';;;;:::::ccccccllooddddollcccc:;;;;,,. .oNWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWXd:;cloxKNWWWWWWWWWWWWOlccllc;,'.'...''',,;::::c:;;:::::::cclllccccc::::;cooccc,.  cNWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWNXK0k:...''oNWWWWWWWWWWWWKdc:ccc:::;;;:::::::cccccc:,,;::::;;::ccccccccc::::o0XK0xc,.. :XMWWWWWWWWWWWWWWWWWWWWWWWW
#MMWWWWWWWWWWWNXkl:;:lll;. .xWWWWWWWWWWWWXxl::cc::::::::::::::c::ccc:,,;::::;;;:ccccccccc:::lkkoll;,,. .cKMWWWMMWWWWWWWWWWWWWWWWWWW
#MMMWWWWWWNKkdooc;,..':lo:':0MWNWWWWWMWMWkc:::cc::::::::::::::::::::;',;;:;;;;;:cc::ccccc:;:lc;,,,,,'...:0MWWWWWWWWWWWWWWWWWWWWWWWW
#MMMWWWWMXd;..,;;clc;..',,cOWMMKkkKWWWWMNd:;;:::::::::::::::::::::;;,'';;;;;,,,,;;;;;:c:::;;;,,,,,,,...':OWWWWWWWWWWWWWWWWWWWWWWWWW
#MMMWWWWWO,.. ...'',,'...;kNWMM0;.xWMWWMXo,;;::::;;;;;;;;;;;;;;;;;;;'.',;;;;,,,'',,''',,,,,,,,''''''..'';kWWMWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWW0;','.. .....',ckNMWMMNdlKWWWWMNo,;,;:;;;;;;;;;;;;;;;;;;;;,'.',,,,,,,,,'''''.'''''''''''...'''cokNWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWNx,';;,.....',,cxKWMMMMWWWWWMWMWx;,,;;;;;;;;;;;;;;;;;,;;;;,'..',,,,,,,,,''''..............''.':lxNWWWMWWWWWWWWWMWWWWWWWWWW
#MWWWWWWWWNk;'',,,,,;,'',:o0NMMMMWWNWWWWWKl,,;;::c:::;;;;;;;;:;,,;;;'..'',,,,,,,,,,,,''''''''''''.......'dNMWWMWWWWWWWWWMWWWWWWWWWW
#MWWWWWWWWWW0l'.''',,,''',;dKWMMMWWNNWWWWW0;,;::;,,,''''''',,;,',,;;'...'''',,,,,,,,,,,'''''''''''......lXWWWKOkOO0XWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWOl,.......'.'l0WMMMWWNXNWWWWXl',,'''''''.......'''',,,,...'''''','''''',,,,''''''''......cKNX0xc;;;;clONWWWWWWWWWMWWW
#MWWWWWWWWWWWWWNKkoc;''',:lx0NWMMWWNXXNWWMNd,'''''...........',''''','....'''''''''''''''''''''''.....;xxoc,'.......:ONWWWWWWWWWMMW
#MWWWWWWWWWWWWWWWWWWNK0KXNWXKNMWWWWNXKKWWWWO:''...............''''.'',......''''''''''''''''''''......;:;;,..........;d0NWWWWMMWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWNKXWMMWNNXK0XWWWNd,'................''','.',..........''''''''''''''...','.',;,'.....   ...;cd0XWWWWMWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWXXWMMWNNXK00NMWWKc'..................','''','................'.......:O0l............   ..',:ldkKNWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWMWWWXXWMMWNNXKOk0WWWW0;...................''''.''''.................'...'xWK:................',,;:lodx0XWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWNKNWMWNXXK0kkXWWWWd.......................'''''.'''.................lXM0;................',;:cooddddkXW
#MWWWWWWWWWWWWWWWWWWWWWWWWWMN0KWMWNXXK0OxkXWWMKc........................'''....'''.............cKWWNc..................',;:looddloK
#MWWWWWWWWWWWWWWWWWWWWWWWWMWKxkNMWNXXK0OkdkXWMWKd,.....................................''''.'.:KWWWWO;...................',:ooddlcd
#MWWWWWWWWWWWWWWWWWWWWWWWWWMN00NWWWXXK0ko:'lXWWWNKd'.........................................'xWWWWWWKl..............   .';:loodocl
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWNKXWWWNKxl;'''cKWWWWWW0,..........         ..................''',kWWWWWWWNO:............   ..,;cooddlc
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWXXNX0dc;,,;oONWWWWWWWXc  ......           .................'''',xWWWWWWWWWNkc..........    .;loodooc:
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWOlllc:;;lkXWWWWNKOkxdc.    ..               ..............''''''dNWWWWWWWWWWNOl'.....'',;;;:lddolc:;o
#MWWWWWWWWWWWWWWWWWWWWWWWMMMWWk;,:coxKNWWWWMNxlxocclc,....             'l,.  ...,,;;;;;:c;''''lXWWWWWWWWWWWWNKx:',::cclooooolc;;:dX
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWMXkxOKNWWWWWWWW0;:xxxdddolc:;'.         .:0W0,.;clxKK0kk0KXNKxdocoKWWWWWWWWWWWWWWWNx;,,;;;;;:::;,;l0NW
#MWWWWWWWWWWWWWWWWWWWWWWWWWMWWWMWMWWWMWWWWWMXc;dkkxxdddlc;.         .cXWNx',d0XNNXKXXXXXNNNNNKd:oXWWWWWWWWWWWWXOo,........''',dXWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWMWWWWWWWK:,coloooolc'....  .  .lXWW0;.,lOKXXXNNNNNNNNXXXOc',kWWWWWWWWWWNx:,....    ...''oXWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWNk,.;lc'..',,'. .  ..  .kWWM0;.':dO0KXXXXXXNXXXXKx;.'xWWWWWWWWWWXl,,'.........',dNWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMO,.';lc.....'.. .      .OWWMX:..':lodxkOOOOkxdoooc...xWWWWWWWWWWNo',,,''...''',oXWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW0:..;::,'.............. ,OWWWWx...'....'cooc,....,,..'kWWWWWWWWWWW0c'........'':OWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWNx'.';::'.........'..'... 'OWWWWK;.......'oOOx:........,OWMWWWWWWMWWWNK0o'.....,lONMWWMWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMWWWKl'.,::;'......'',:,,,'... ,KWWWWNo.......';ccc:,'.....'c0WWWWWWWWWWWWWWWNx;,:okKNWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWNOlcc:;;;'...'''.,coc.''.....:KWWWWWk'......',:lcc;'.....,o0WWWWWWMWWWWWWWWWWXXWWWWWWWWMWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWNXKXWWNKOx:.'',,'',::'..',,',,dNWWWWWO;,'.....';cc:,......,lOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXXNWMWWMWWWWKd:,,'';'.',;;;:ldOKNMWWMWW0c,......',;:;,'.....:d0WWWWWWWWWWWWWWWWWWWWMWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWMWWWWMWKOXWWWWWWWWWWWWNKd,'..,;::ldk0NWWMMWWWMWWXo,,'....',,;;,'.....:d0WWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWMMWWWWKoo0XNWWWWWNKOxollc;,:cclxOXWWWWWWWWWWWWWWNo',,...,;;;,,,'.....,:OWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWMWWMWNx:ccldxxxxdlc;;;,;cldxxOXWWWWWWWWWWWMWWWWWWd',,;ckKXXXXXK0Oo;'.',xWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXkoc::::cccc::ccloxOOOOXWWWWWWWMWWWWWWWWWWWWx,ckKNWMWWWMWWWWNK0xl,:0WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWMMWWWWWKxoddxxxxxkkkkOO000KKXWWWWWWWWWWWWWWWWWWWWWWx:kNWWWWMMMMMWWWWWNNXx;cKMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWMMWWWWN0xddolodxkO0KXXNNWMMMWWWWWWWWWWWWWWWWWWWWKo,:kWWMMMMMWWWWWWWN0l;,;kWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWNK000KXNWWWWWMMWWMMWWWWWWWWWWWWWWWWWWWk::;:ok00KKXXXXXKOxl;',,;xNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWWWWWWWWWWWWWWWXkl;cc:::ccllooolc:;,,,,;lxKWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW0xkdlc:;:::cllollc::;;:ldkx0WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOodk00kxddooooooooddxkOOkddKWWWWMWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNOoc:cldxkkOOO000OOkxollokXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXkoc::;:::::::::clokKNMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNXXXKKKXNWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMWWWWWWWWWWWWWWMWWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWMWWWWWWWWMWWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWM
#MMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMM
#MMWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM