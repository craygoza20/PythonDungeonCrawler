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
# TODO: Create a shopping loop function
# TODO: Create actions menu
#-------------------------------------------------------------------------------------------------------------------#
# Characters

# There will be three main groups
# Player, Enemy, NPC

class Character:
    
    inventory = {}
    health = 0
    coins = 0
    attackPower = 0
    defensePower = 0
    currentLocation = {}

    def __init__(self, name, level, group, coins=0, health=8, attackPower=5, defensePower=2):
        self.name = name
        self.level = level
        self.group = group
        if self.group == 'Player':
            self.health = 15
            self.attackPower = 6
            self.defensePower = 2
            self.coins = 20
            self.inventory = {"potions": 0, "weapon": "knife", "arrows": 0, "shield": "none", "armor": "none"}
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
            {self.name}'s attack power is {self.attackPower}. {self.name}'s defense power is {self.defensePower}.
            Currently in your inventory: {self.inventory}."""
        elif self.group == 'Enemy': # TODO: add repr for Enemies
            return f"This is a level {self.level} {self.name} with {self.health} points of health."
            pass
        elif self.group == 'NPC': # TODO: add repr for NPC (shopkeeps)
            pass    
    
    # TODO: need actions for characters (attack, use items, buy items, talk to others, etc..)

    def levelUp(self, nextLevel):
        self.level = nextLevel
        self.health = 15 + (nextLevel * 1.5)
        self.attackPower += self.attackPower + (nextLevel * 1.5)
        self.defensePower += 2
        return f"""
        {self.name} has leveled up! {self.name} is now level {self.level}.
        Health increased to {self.health} points.
        Attack power has increased to {self.attackPower} points.
        Defense power has increased to {self.defensePower} points.

        Huzzah!
        """
    
    def attack(self, enemy):
        if(enemy.defensePower > 0):
            attackpoints = self.attackPower * (1 / enemy.defensePower)
        else:
            attackpoints = self.attackPower

        enemy.health -= attackpoints
        print("\n" + f"{self.name} has attacked {enemy.name} for {attackpoints} health.")
        if self.health > 0:
            if enemy.health <= 0:
                print(f"{enemy.name} has been slain by {self.name}.")
            else:
                print(f"{enemy.name} has {enemy.health} health points remaining." + "\n")
    
    def useItem(self, item):
        pass

    def buyItem(self, item, shopkeep):
        pass

    def speak(self, NPC):
        pass

    def setLocation(self, location):
        self.currentLocation = location
        return print(f'You are now located at the {self.currentLocation}.')

#-------------------------------------------------------------------------------------------------------------------#
# Location system
# TODO: Create locations
# maybe a 2d list? i.e. locations[[zone, specific area]]
# where zone = town, forest, dungeon
# town areas = different shops, roadside inn, town square
# forest areas = lonely road, stream, dense brush
# dungeon areas = entrance, corridor, treasure rooms, trapped rooms

zones = ["town", "forest", "dungeon"]
areas = [
        ["town square", "inn", "potion stand", "blacksmith"], 
        ["lonely road", "stream", "dense brush"],
        ["entrance", "corridor", "treasure room", "trapped room"]
        ]

locations = dict(zip(zones, areas))

def choose_location():
    pass


#-------------------------------------------------------------------------------------------------------------------#
# Combat loop

# TODO: items need to be added

def combat(player, enemy):
    combatActive = True
    while (player.health > 0) and (enemy.health > 0) and combatActive:
        # Player attack turn
        playerChoice = int(input("Choose a number:\n1.Attack\n2.Use Item\n3.Flee\n"))
        if playerChoice == 1:
            player.attack(enemy)
        if playerChoice == 2:
            # needs a list of items to choose
            #player.useItem()
            pass
        if playerChoice == 3:
            print(f"Your current health is at {player.health} points.")
            print("You will lose 3 health points if you decide to flee, are you sure? \n")
            fleeChoice = input("Yes (Y) / No (N)")
            fleeChoice = fleeChoice.lower()
            if fleeChoice == 'yes' or fleeChoice == 'y':
                if player.health <= 0:
                    print("You have died in the process of fleeing.")
                    gameOver = True
                    combatActive = False
                else:
                    player.health -= 3
                    print("You have taken 3 points of damage while fleeing.")
                    print(f"You now have {player.health} health points remaining." + "\n")
                    combatActive = False
        # Enemy attack turn
        if enemy.health > 0:
            enemy.attack(player)
        else:
            combatActive = False

#-------------------------------------------------------------------------------------------------------------------#
# Shopping loop
# TODO: Create a loop for interacting with shopkeeps
# TODO: Create items list for each shopkeep

def shop():
    pass

# core items:
# Health potion
# sword, shield
# bow, arrows
# map? (guide to loot)


#-------------------------------------------------------------------------------------------------------------------#
# actions menu

# TODO: Define actions a character can do after each event (goto, view inventory, view status, etc...)
def actions():
    pass

#-------------------------------------------------------------------------------------------------------------------#
# main game

def main():
    gameOver = False
    c_name = input("Please type in your character's name: ")
    player = Character(c_name, 1, 'Player')
    print(player)

    print("""
    The warmth of the sun radiates across your body.
    Birds are chirping, the leaves are rustling from the breeze.
    The cool morning air penetrates your nostrils.
    Dirt, moss, a hint of wintergreen.
    \"Where am I?\", you ask yourself.
    You hear a faint snort coming from behind.
    """)
    # first branching path
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
        boar = Character("Boar", 1, "Enemy", 0, 10, 2, 0)
        combat(player, boar)
        print(player.levelUp(2))
    else:
        print("""
        You decide to head the opposite direction.
        """)
    
    print("""
    After walking for a little while, you find a dirt road and decide to follow it.
    """)
    player.setLocation(locations['town'][0]) # town square
    print("""
    You see a map with various locations:
    1. Town Square (You are here)
    2. Inn
    3. Potion Stand
    4. Blacksmith
    """)
    new_loc = input("Where do you wish to go? (select number)")

if __name__ == "__main__":
    main()
