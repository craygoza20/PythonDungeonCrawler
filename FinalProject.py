"""
Created by: Carlos Raygoza
Date: 2/22/2022
Description: A small text adventure game where you will be able to create your own
             character and go on a few quests!

Sources: Codecademy Python3 course, W3Schools, StackOverflow

"""

# TODO: Create class for characters (Player, Enemies, NPCs)
# TODO: Create system for locations
# TODO: Create quest lines
# TODO: Create a combat loop function
# TODO: Create a shopping loop function


# There will be three main groups
# Player, Enemy, NPC


class Character:
    
    inventory = {}
    health = 0
    coins = 0
    attackPower = 0
    defensePower = 0

    def __init__(self, name, level, group, coins=0, health=8, attackPower=5, defensePower=2):
        self.name = name
        self.level = level
        self.group = group
        if self.group == 'Player':
            self.health = 15
            self.attackPower = 6
            self.defensePower = 2
            self.coins = 20
        else:
            self.health = health
            self.attackPower = attackPower
            self.defensePower = defensePower
            self.coins = coins

    def __repr__(self):
        if self.group == 'Player':
            return f"""
            Your character is named {self.name}. {self.name} is level {self.level}. 
            {self.name} has {self.coins} coins.
            {self.name}'s attack power is {self.attackPower}. {self.name}'s defense power is {self.defensePower}."""
        elif self.group == 'Enemy': # TODO: add repr for Enemies
            pass
        elif self.group == 'NPC': # TODO: add repr for NPC (shopkeeps)
            pass    
    
    # TODO: need actions for characters (attack, use items, buy items, talk to others, etc..)
    
    def attack(self, enemy):
        attackpoints = self.attackPower * (1 / enemy.defensePower)
        enemy.health -= attackpoints
        print(f"{self.name} has attacked {enemy.name} for {attackpoints} health.")
        if enemy.health <= 0:
            print(f"{enemy.name} has been slain by {self.name}.")
        else:
            print(f"{enemy.name} has {enemy.health} health points remaining.")
    
    # FIXME: Combat loop only allows player to attack, need enemy to attack also
    def combat(self, enemy):
        combatActive = True
        while (self.health > 0) and (enemy.health > 0) and combatActive:
            playerChoice = int(input("Choose a number:\n1. Attack\n2.Use Item\n3.Flee"))
            if playerChoice == 1:
                self.attack(enemy)
            if playerChoice == 2:
                self.useItem()
            if playerChoice == 3:
                print(f"Your current health is at {self.health} points.")
                print("You will lose 3 health points if you decide to flee, are you sure?")
                fleeChoice = input("Yes (Y) / No (N)")
                if fleeChoice == 'Yes' or fleeChoice == 'Y':
                    if self.health <= 0:
                        print("You have died in the process of fleeing.")
                        gameOver = True
                        combatActive = False
                    else:
                        self.health -= 3
                        print("You have taken 3 points of damage while fleeing.")
                        print(f"You now have {self.health} health points remaining.")
                        combatActive = False
    def useItem(self, item):
        pass

    def buy(self, item, shopkeep):
        pass

    def speak(self, NPC):
        pass

gameOver = False
c_name = input("Please type in your character's name: ")
player = Character(c_name, 1, 'Player')
print(player)

print("""
The warmth of the sun radiates across your body.
Birds are chirping, the leaves are rustling from the breeze.
The cool morning air penetrates your nostrils.
Dirt, moss, a hint of wintergreen.
\"Where am I?\"
You hear a faint snort coming from behind.
""")

choice1 = int(input("""
Choose a number:
1. Go towards the noise.
2. Get away from the noise.
"""))

if choice1 == 1:
    print("""
    You go towards the source of the noise and find yourself face to face with a wild boar!
    The boar begins to squeal and is preparing to charge at you!
    """)
