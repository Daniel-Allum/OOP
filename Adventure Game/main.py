from character import Enemy, Friend
from cave import Cave
from item import Item

cavern = Cave('Cavern')
cavern.set_description('A damp and dirty cave.')

grotto = Cave('Grotto')
grotto.set_description('A small cave with ancient graffiti.')

dungeon = Cave('Dungeon')
dungeon.set_description('A large cave with a crack.')

cavern.link_cave(dungeon, 'south')
grotto.link_cave(dungeon, 'east')
dungeon.link_cave(grotto, 'west')
dungeon.link_cave(cavern, 'north')

bag = []
torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
dungeon.set_item(torch)

vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")
grotto.set_item(vegemite)

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)
josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

current_cave = cavern
dead = False
while dead == False:
    item = current_cave.get_item()
    if item is not None:
        item.describe()
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    current_cave = current_cave.move(command)
    if command in ['north', 'south', 'east', 'west']:
            current_cave = current_cave.move(command)
    elif command == 'talk':
        if inhabitant is not None:
            inhabitant.talk()

    elif command == 'fight':
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Bravo,hero you won the fight!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                            print('Congratulations, you have survived another adventure')
                            dead = True
                else:
                    print("Scurry home, you lost the fight.")
                    print("That,s the end of the game")
            else:
                print("You don't have a " + fight_with)
        else:
            print('There is no one here to fight with')

    elif command == 'pat':
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn’t do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")

    elif command == 'take':
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_room.set_item(None)
