zones = ["town", "forest", "dungeon"]
areas = [
        ["blacksmith", "potion stand", "inn", "town square"], 
        ["lonely road", "stream", "dense brush"],
        ["entrance", "corridor", "treasure room", "trapped room"]
        ]

locations = dict(zip(zones, areas))
print(locations)

for locations in locations.items():
    print(locations)
    