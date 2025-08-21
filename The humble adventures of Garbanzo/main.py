from character import Character, NPC, Enemy
from room import Room
from item import Item, HealthPotion, Key, Torch, Weapon

def setup_world():
    rooms = {}
    rooms['foyer'] = Room("Foyer")
    rooms['foyer'].set_description("The dimly lit foyer of the old house. The main exit door is locked tight.")

    rooms['library'] = Room("Library")
    rooms['library'].set_description("Shelves of dusty books. A faint whisper can be heard.")

    rooms['kitchen'] = Room("Kitchen")
    rooms['kitchen'].set_description("Old kitchen with broken utensils. There's a foul smell.")

    rooms['hallway'] = Room("Hallway")
    rooms['hallway'].set_description("A long hallway with flickering lights.")

    rooms['basement'] = Room("Basement")
    rooms['basement'].set_description("A cold, dark basement. You hear mechanical noises.")

    rooms['study'] = Room("Study")
    rooms['study'].set_description("A cluttered study with papers scattered everywhere.")

    rooms['bedroom'] = Room("Bedroom")
    rooms['bedroom'].set_description("A dusty bedroom with a creaky bed.")

    rooms['attic'] = Room("Attic")
    rooms['attic'].set_description("A cramped attic filled with old furniture.")


    rooms['foyer'].link_room(rooms['library'], 'north')
    rooms['foyer'].link_room(rooms['kitchen'], 'east')
    rooms['library'].link_room(rooms['foyer'], 'south')
    rooms['library'].link_room(rooms['hallway'], 'east')
    rooms['kitchen'].link_room(rooms['foyer'], 'west')
    rooms['kitchen'].link_room(rooms['basement'], 'down')
    rooms['hallway'].link_room(rooms['library'], 'west')
    rooms['hallway'].link_room(rooms['study'], 'north')
    rooms['hallway'].link_room(rooms['bedroom'], 'east')
    rooms['basement'].link_room(rooms['kitchen'], 'up')
    rooms['study'].link_room(rooms['hallway'], 'south')
    rooms['study'].link_room(rooms['attic'], 'up')
    rooms['bedroom'].link_room(rooms['hallway'], 'west')
    rooms['attic'].link_room(rooms['study'], 'down')


    key1 = Key("Rusty Key", "Main Door", short_name="key1")
    key1.set_description("An old rusty key, looks like it might open the main exit door.")
    key2 = Key("Silver Key", "Main Door", short_name="key2")
    key2.set_description("A shiny silver key, seems important.")
    key3 = Key("Golden Key", "Main Door", short_name="key3")
    key3.set_description("A golden key with intricate engravings.")

    potion_small = HealthPotion("Small Health Potion", short_name="potion", heal_amount=50, weight=1)
    potion_small.set_description("A small vial filled with red liquid. Restores some health.")
    potion_large = HealthPotion("Large Health Potion", short_name="bigpotion", heal_amount=80, weight=2)
    potion_large.set_description("A large vial that restores a significant amount of health.")

    torch = Torch("Wooden Torch", short_name="torch")
    torch.set_description("A wooden torch. Can be lit to brighten dark areas.")

    sword = Weapon("Rusty Sword", "An old sword with a dull blade.", 4, 0, damage=10, weapon_type="Melee", short_name="sword")
    shotgun = Weapon("Shotgun", "A powerful shotgun with limited shells.", 7, 0, damage=35, weapon_type="Ranged", short_name="shotgun")
    laser_pistol = Weapon("Laser Pistol", "Small laser pistol.", 3, 0, damage=12, weapon_type="Ranged", short_name="pistol")


    rooms['kitchen'].add_item(potion_small)
    rooms['foyer'].add_item(torch)
    rooms['bedroom'].add_item(key1)
    rooms['attic'].add_item(shotgun)
    rooms['study'].add_item(key2)
    rooms['hallway'].add_item(potion_large)
    rooms['library'].add_item(key3)
    rooms['basement'].add_item(sword)


    luther = NPC("Luther", rooms['library'], "I can help you survive this place. Stay alert!")
    rooms['library'].set_character(luther)

    zlatko = Enemy("Zlatko", rooms['basement'], health=100, damage=20, drop_item=shotgun)
    zlatko.inventory.append(shotgun)
    rooms['basement'].set_character(zlatko)

    droid1 = Enemy("Security Droid 1", rooms['hallway'], health=50, damage=10, drop_item=laser_pistol)
    droid1.inventory.append(laser_pistol)
    rooms['hallway'].set_character(droid1)

    droid2 = Enemy("Security Droid 2", rooms['kitchen'], health=40, damage=8, drop_item=laser_pistol)
    droid2.inventory.append(laser_pistol)
    rooms['kitchen'].set_character(droid2)

    return rooms, zlatko

def player_has_all_keys(player):
    keys_found = [item for item in player.inventory if isinstance(item, Key) and item.unlocks == "Main Door"]
    return len(keys_found) == 3

def print_help():
    print("""
Commands:
    go [direction]      -- Move in a direction (north, south, east, west, up, down, out)
    talk                -- Talk to an NPC in the room
    attack              -- Attack an enemy in the room
    take [item]         -- Take an item from the room (or just 'take')
    drop [item]         -- Drop an item from your inventory (use short name)
    inventory           -- Show your inventory
    use [item]          -- Use an item in your inventory (use short name)
    health              -- Show your current health
    help                -- Show this help message
    quit                -- Exit the game
""")

def main():
    rooms, zlatko = setup_world()
    player = Character("Player", rooms['foyer'])
    zlatko_defeated = False

    print("Welcome to Zlatkos Mansion!")
    print_help()
    player.display_current_room()

    while True:
        command = input("\n> ").strip().lower()
        if not command:
            continue

        if command == 'quit':
            print("Thanks for playing! Goodbye.")
            break

        elif command.startswith("go "):
            direction = command[3:]

            if direction == "out":
                if player.current_room.get_name() != "Foyer":
                    print("You can't go that way.")
                    continue
                if not player_has_all_keys(player):
                    print("The main door is locked tight. You must first collect all 3 keys.")
                    continue
                if not zlatko_defeated:
                    print("As you try to leave, Zlatko appears, blocking your way!")
                    while zlatko.health > 0 and player.health > 0:
                        print(f"\nYour Health: {player.health} | Zlatko's Health: {zlatko.health}")
                        action = input("Attack or use item? ").strip().lower()
                        if action == "attack":
                            weapon = next((item for item in player.inventory if isinstance(item, Weapon)), None)
                            if weapon:
                                dmg = weapon.damage
                                print(f"You attack Zlatko with {weapon.get_name()}, dealing {dmg} damage!")
                            else:
                                dmg = 10
                                print(f"You attack Zlatko with your fists, dealing {dmg} damage!")
                            zlatko.health -= dmg
                        elif action.startswith("use "):
                            item_name = action[4:]
                            player.use_item(item_name)
                        else:
                            print("Invalid action. Type 'attack' or 'use [item]'.")
                            continue

                        if zlatko.health <= 0:
                            print("Zlatko is defeated!")
                            zlatko_defeated = True
                            zlatko.on_defeat()
                            player.current_room.remove_character()
                            break

                        zlatko.attack(player)
                        if player.health <= 0:
                            print("You have been defeated. Game Over.")
                            return

                    print("You use the 3 keys to unlock the main door and step outside. You have escaped!")
                    break
                else:
                    print("The door is open. You step outside. You have escaped!")
                    break

            else:
                player.move(direction)

        elif command == "talk":
            character = player.current_room.get_character()
            if isinstance(character, NPC):
                character.talk()
            else:
                print("There is no one here to talk to.")

        elif command == "attack":
            character = player.current_room.get_character()
            if isinstance(character, Enemy):
                character.attack(player)
                if player.health <= 0:
                    print("You have been defeated. Game Over.")
                    break

                weapon = next((item for item in player.inventory if isinstance(item, Weapon)), None)
                if weapon:
                    dmg = weapon.damage
                    print(f"You attack {character.get_name()} with {weapon.get_name()}, dealing {dmg} damage!")
                else:
                    dmg = 10
                    print(f"You attack {character.get_name()} with your fists, dealing {dmg} damage!")
                character.health -= dmg
                if character.health <= 0:
                    print(f"{character.get_name()} is defeated!")
                    character.on_defeat()
                    player.current_room.remove_character()
            else:
                print("There is no enemy here to attack.")

        elif command.startswith("take"):
            parts = command.split(' ', 1)
            if len(parts) == 1:
                player.pick_up()
            else:
                requested_name = parts[1].lower()
                item = player.current_room.get_items()
                if item and (requested_name == item.get_short_name() or requested_name == item.get_name().lower()):
                    player.pick_up()
                else:
                    print(f"There is no '{requested_name}' here to take.")

        elif command.startswith("drop "):
            item_name = command[5:].lower()
            player.drop_item(item_name)

        elif command == "inventory":
            if player.inventory:
                print("You have:")
                for item in player.inventory:
                    print(f" - {item.get_name()} (\"{item.get_short_name()}\")")
                print(f"Total weight: {player.get_current_weight()} kg / {player.max_weight} kg")
            else:
                print("Your inventory is empty.")

        elif command.startswith("use "):
            item_name = command[4:].lower()
            player.use_item(item_name)

        elif command == "health":
            print(f"Your health: {player.get_health()}")

        elif command == "help":
            print_help()

        else:
            print("I don't understand that command. Type 'help' for a list of commands.")

main()