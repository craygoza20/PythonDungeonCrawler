from FinalProject import Character

print("Initializing combat test")

unit1 = Character('Rey', 1, 'Player')
unit2 = Character('Not Rey', 1, 'Player')

print(unit1)
print(unit2)

unit1.combat(unit2)