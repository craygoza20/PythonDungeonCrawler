from FinalProject import Character

print("Initializing combat test")

unit1 = Character('Rey', 1, 'Player')
unit2 = Character('Not Rey', 1, 'Player')

print(unit1)
print(unit2)



# FIXME: items need to be added
def combat(player, enemy):
    combatActive = True
    while (player.health > 0) and (enemy.health > 0) and combatActive:
        # Player attack turn
        playerChoice = int(input("Choose a number:\n1. Attack\n2.Use Item\n3.Flee"))
        if playerChoice == 1:
            player.attack(enemy)
        if playerChoice == 2:
            # needs a list of items to choose
            #player.useItem()
            pass
        if playerChoice == 3:
            print(f"Your current health is at {player.health} points.")
            print("You will lose 3 health points if you decide to flee, are you sure?")
            fleeChoice = input("Yes (Y) / No (N)")
            if fleeChoice == 'Yes' or fleeChoice == 'Y':
                if player.health <= 0:
                    print("You have died in the process of fleeing.")
                    gameOver = True
                    combatActive = False
                else:
                    player.health -= 3
                    print("You have taken 3 points of damage while fleeing.")
                    print(f"You now have {player.health} health points remaining.")
                    combatActive = False
        # Enemy attack turn
        if enemy.health > 0:
            enemy.attack(player)
        else:
            combatActive = False

combat(unit1, unit2)
print(unit1.health)