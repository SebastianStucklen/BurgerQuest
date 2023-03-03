import random
import time
global playerHealth, hasShield, sword, hasPotion, hasArmor, defending, bossIsAttacking
#other things
room = 10
choice = "PLACEHOLDER"
bossIsAttacking = False
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
playerHealth = 100
#item variables
inventory = []
hasShield = True
sword = 7
#change this to 15 when player gets upgraded sword
hasPotion = True
hasArmor = True
defending = False
#boss fight
def bossFight(bossHealth,damage):
	global playerHealth, hasShield, sword, hasPotion, hasArmor, defending, bossIsAttacking
	while bossHealth >= 0 or playerHealth >= 0:
		print("Boss health:")
		print(bossHealth)
		print("Your health")
		print(playerHealth)
		if bossIsAttacking == False:
			if hasShield == False and hasPotion == False:
				print("you can attack")
				choice = input()
			elif hasShield == True and hasPotion == False:
				print("you can attack or defend")
				choice = input()
			elif hasShield == True and hasPotion == True:
				print("you can attack, defend, or use a potion")
				choice = input()
			if choice == 'attack':
				bossHealth-=sword
				print("you attack!")
				bossIsAttacking = True
			elif choice == 'defend':
				defending = True
				print("you ready your shield")
				bossIsAttacking = True
			elif choice == 'potion':
				print("you drink your potion")
				if playerHealth < 100:
					playerHealth+=50
				if playerHealth > 100:
					playerHealth=100
				bossIsAttacking = True
			else:
				print("not an option")
		if bossIsAttacking == True:
			print("the boss attacks!")
			if defending == False:
				playerHealth-=damage
			if defending == True:
				playerHealth-=damage/2
			bossIsAttacking = False
		#return playerHealth and bossHealth
def northBoss():
	print("test")
	bossFight(100,10)
#help
def help():
    #put stuff here
    print("Type I to view inventory")
while choice != "quit" or playerHealth > 0:
	if room == 1:
		choice = input("You are in a grand hall. There are four doors. north, east, south, and west.")
		if choice == 'help':
			help()
	#playerHealth = -100
	#bossFight(100,34)

print("you dead")