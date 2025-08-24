from character import Character, NPC, Enemy
from room import Room #Imports the classes and all the code
from item import Item, HealthPotion, Key, Torch, Weapon

def setup_world(): #Creates a function
    rooms = {} #Creates an empty dictionary called rooms
    rooms['foyer'] = Room("Foyer") #Creates the room called Foyer
    rooms['foyer'].set_description("The dimly lit foyer of the old house. The main exit door is locked tight.") #sets the room description

    rooms['library'] = Room("Library") #Creates the room called Library
    rooms['library'].set_description("Shelves of dusty books. A faint whisper can be heard.") #sets the room description

    rooms['kitchen'] = Room("Kitchen") #Creates the room called Kitchen
    rooms['kitchen'].set_description("Old kitchen with broken utensils. There's a foul smell.") #sets the room description

    rooms['hallway'] = Room("Hallway") #Creates the room called Hallway
    rooms['hallway'].set_description("A long hallway with flickering lights.") #sets the room description

    rooms['basement'] = Room("Basement") #Creates the room called Basement
    rooms['basement'].set_description("A cold, dark basement. You hear mechanical noises.") #sets the room description

    rooms['study'] = Room("Study") #Creates the room called Study
    rooms['study'].set_description("A cluttered study with papers scattered everywhere.") #sets the room description

    rooms['bedroom'] = Room("Bedroom") #Creates the room called Bedroom
    rooms['bedroom'].set_description("A dusty bedroom with a creaky bed.") #sets the room description

    rooms['attic'] = Room("Attic") #Creates the room called Attic
    rooms['attic'].set_description("A cramped attic filled with old furniture.") #sets the room description


    rooms['foyer'].link_room(rooms['library'], 'north') #Links the foyer to the library
    rooms['foyer'].link_room(rooms['kitchen'], 'east') #Links the foyer to the kitchen
    rooms['library'].link_room(rooms['foyer'], 'south') #Links the Library to the foyer
    rooms['library'].link_room(rooms['hallway'], 'east') #Links the Library to the hallway
    rooms['kitchen'].link_room(rooms['foyer'], 'west') #Links the kitchen to the foyer
    rooms['kitchen'].link_room(rooms['basement'], 'down') #Links the kitchen to the basement
    rooms['hallway'].link_room(rooms['library'], 'west') #Links the hallway to the library
    rooms['hallway'].link_room(rooms['study'], 'north') #Links the hallway to the study
    rooms['hallway'].link_room(rooms['bedroom'], 'east') #Links the hallway to the bedroom
    rooms['basement'].link_room(rooms['kitchen'], 'up') #Links the basement to the kitchen
    rooms['study'].link_room(rooms['hallway'], 'south') #Links the study to the hallway
    rooms['study'].link_room(rooms['attic'], 'up') #Links the study to the attic
    rooms['bedroom'].link_room(rooms['hallway'], 'west') #Links the bedroom to the hallway
    rooms['attic'].link_room(rooms['study'], 'down') #Links the attic to the study

    key1 = Key("Rusty Key", "Main Door", short_name="key1") #Creates an item called Key1 and sets location, full name and shortname
    key1.set_description("An old rusty key, looks like it might open the main exit door.") #Sets the keys description
    key2 = Key("Silver Key", "Main Door", short_name="key2") #Creates an item called Key2 and sets location, full name and shortname
    key2.set_description("A shiny silver key, seems important.") #Sets the keys description
    key3 = Key("Golden Key", "Main Door", short_name="key3") #Creates an item called Key3 and sets location, full name and shortname
    key3.set_description("A golden key with intricate engravings.") #Sets the keys description

    potion_small = HealthPotion("Small Health Potion", short_name="potion", heal_amount=50, weight=1) #Creates a small potion with unique attributes
    potion_small.set_description("A small vial filled with red liquid. Restores some health.") #Sets the small health potions description
    potion_large = HealthPotion("Large Health Potion", short_name="bigpotion", heal_amount=80, weight=2) #Creates a large potion with unique attributes
    potion_large.set_description("A large vial that restores a significant amount of health.") #Sets the large health potions description

    torch = Torch("Wooden Torch", short_name="torch") #Creates the torch item
    torch.set_description("A wooden torch. Can be lit to brighten dark areas.") #Sets the torch description

    sword = Weapon("Rusty Sword", "An old sword with a dull blade.", 4, 0, damage=10, weapon_type="Melee", short_name="sword") #Creates the sword object with its unique attributes
    shotgun = Weapon("Shotgun", "A powerful shotgun with limited shells.", 7, 0, damage=35, weapon_type="Ranged", short_name="shotgun") #Creates the shotgun object with its unique attributes
    laser_pistol = Weapon("Laser Pistol", "Small laser pistol.", 3, 0, damage=12, weapon_type="Ranged", short_name="pistol") #Creates the pistol object with its unique attributes


    rooms['kitchen'].add_item(potion_small) #Sets the potion_small to the kitchen
    rooms['foyer'].add_item(torch) #Sets the torch to the foyer
    rooms['bedroom'].add_item(key1) #Sets the key1 to the bedroom
    rooms['attic'].add_item(shotgun) #Sets the shotgun to the attic
    rooms['study'].add_item(key2) #Sets the key2 to the study
    rooms['hallway'].add_item(potion_large) #Sets the potion_large to the hallway
    rooms['library'].add_item(key3) #Sets the key3 to the library
    rooms['basement'].add_item(sword) #Sets the sword to the basement


    luther = NPC("Luther", rooms['library'], "I can help you survive this place. Stay alert!") #creates an NPC called Luther, dislpays his room and creates his dialogue
    rooms['library'].set_character(luther) #Sets Luther to the library

    zlatko = Enemy("Zlatko", rooms['basement'], health=100, damage=20, drop_item=shotgun) #creates an Enemy called Zlatko, dislpays his room and sets his health damage and his item he drops
    zlatko.inventory.append(shotgun) #Gives Zlatko a shotgun
    rooms['basement'].set_character(zlatko) #Sets Zlatko to the basement

    droid1 = Enemy("Security Droid 1", rooms['hallway'], health=50, damage=10, drop_item=laser_pistol) #creates an Ememy called droid1, dislpays his room and sets his health damage and his item he drops
    droid1.inventory.append(laser_pistol) #Gives the security droid a laser pistol
    rooms['hallway'].set_character(droid1) #Sets the droid1 to the hallway

    droid2 = Enemy("Security Droid 2", rooms['kitchen'], health=40, damage=8, drop_item=laser_pistol) #creates an Enemy droid2, dislpays his room and sets his health damage and his item he drops
    rooms['kitchen'].set_character(droid2) #Sets the droid2 to the kitchen

    return rooms, zlatko #returns Zlatko separately so main() can track him directly, without having to search through the rooms dictionary.

def player_has_all_keys(player): #Creates a function called player_has_all_keys(player)
    keys_found = [item for item in player.inventory if isinstance(item, Key) and item.unlocks == "Main Door"]
    return len(keys_found) == 3 #This code checks if the list length of keys is 3 if so then the main door is unlocked

def print_help(): #Creates a function called print_help
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
""") #Command log

def main(): #Creates the main game loop
    rooms, zlatko = setup_world() #Setsup the world (rooms/characters)
    player = Character("Player", rooms['foyer']) #Starts the character in the foyer
    zlatko_defeated = False #Makes it so Zlatko is alive

    print("Welcome to Zlatkos Mansion!") #Welcome message
    print_help() #Prints the command log
    player.display_current_room() #Prints the foyers description

    while True: #Makes game loop keep running until it is told
        command = input("\n> ").strip().lower() #Asks for an input, cleansup spacing and converts to lowercase
        if not command: 
            continue #If no command is typed continue on

        if command == 'quit': #Creates quit
            print("Thanks for playing! Goodbye.")
            break #Ends the game

        elif command.startswith("go "): #Creates command go
            direction = command[3:] #Removes the first three characters 'go ' to only read the direction

            if direction == "out": #Creates direction called out
                if player.current_room.get_name() != "Foyer": #Sees if you arent in the foyer
                    print("You can't go that way.") #Prints invalid direction text
                    continue
                if not player_has_all_keys(player): #Checks if you have all keys in the foyer
                    print("The main door is locked tight. You must first collect all 3 keys.")
                    continue
                if not zlatko_defeated: #If zlatko still alive
                    print("As you try to leave, Zlatko appears, blocking your way!")
                    while zlatko.health > 0 and player.health > 0: #Starts the combat loop
                        print(f"\nYour Health: {player.health} | Zlatko's Health: {zlatko.health}") #Prints both health bars
                        action = input("Attack or use item? ").strip().lower() #prints if you want to attack or use item
                        if action == "attack": #If attack is written
                            weapon = next((item for item in player.inventory if isinstance(item, Weapon)), None) #Checks your best weapon
                            if weapon: #If you do have a weapon
                                dmg = weapon.damage #Customizable weapon damage
                                print(f"You attack Zlatko with {weapon.get_name()}, dealing {dmg} damage!") #Shows the damage you delt
                            else: #If no weapon
                                dmg = 10 #Hardcoded fist damage
                                print(f"You attack Zlatko with your fists, dealing {dmg} damage!") #Displays damage
                            zlatko.health -= dmg #Minuses damage dealt from his health
                        elif action.startswith("use "): #If use is written
                            item_name = action[4:] #Cuts off the command "use " and only registers the last part
                            player.use_item(item_name) #Displays what you used
                        else:
                            print("Invalid action. Type 'attack' or 'use [item]'.") #Message if didnt type the two commands
                            continue #Continues your turn

                        if zlatko.health <= 0: #Checks if Zlatkos health is below zero
                            print("Zlatko is defeated!")
                            zlatko_defeated = True #Sets boolean value to True
                            zlatko.on_defeat() #drops item
                            player.current_room.remove_character() #removes player from the room
                            break #Ends the combat loop

                        zlatko.attack(player) #Zlatko attacks
                        if player.health <= 0: #Checks if players health reaches below 0
                            print("You have been defeated. Game Over.")
                            return #Ends the whole game loop

                    print("You use the 3 keys to unlock the main door and step outside. You have escaped!")
                    break #Displays final text for this win condition and ends the game
                else:
                    print("The door is open. You step outside. You have escaped!")
                    break #Displays final text for this win condition and ends the game

            else:
                player.move(direction) #Default move method in the main game loop

        elif command == "talk": #Creates talk command
            character = player.current_room.get_character() #Checks room for characters
            if isinstance(character, NPC): #If there is characters and an NPC
                character.talk() #Displays set character dialogue
            else:
                print("There is no one here to talk to.") #Else prints this dialogue

        elif command == "attack": #Creates basic attack command
            character = player.current_room.get_character() #Checks room for characters
            if isinstance(character, Enemy): #If there is characters and an enemy
                character.attack(player) #Enemy attacks you
                if player.health <= 0: #If health is below zero
                    print("You have been defeated. Game Over.")
                    break #Ends the game if defeated

                weapon = next((item for item in player.inventory if isinstance(item, Weapon)), None) #Checks inventory for weapon
                if weapon: #If you have a weapon
                    dmg = weapon.damage #Sets the weapon damage to this variable
                    print(f"You attack {character.get_name()} with {weapon.get_name()}, dealing {dmg} damage!") #Weapon printed out
                else:
                    dmg = 10 #If you have no weapon then use harcoded fist damage
                    print(f"You attack {character.get_name()} with your fists, dealing {dmg} damage!") #Fist attack printed out
                character.health -= dmg #Minuses damage variable from enemy health
                if character.health <= 0: #If enemy health is below zero
                    print(f"{character.get_name()} is defeated!") #Display you defeated them
                    character.on_defeat() #Drops item
                    player.current_room.remove_character() #Removes them from the room
            else:
                print("There is no enemy here to attack.") #If no enemy prints this

        elif command.startswith("take"):
            parts = command.split(' ', 1) #splits the command into parts
            if len(parts) == 1: #if only take was wrote then pickup whatever is in the room
                player.pick_up()
            else: #otherwise check if the item wanted is there
                requested_name = parts[1].lower()
                item = player.current_room.get_items()
                if item and (requested_name == item.get_short_name() or requested_name == item.get_name().lower()):
                    player.pick_up() #Check the shortname or the full name to pick up
                else:
                    print(f"There is no '{requested_name}' here to take.") #if the item is not there

        elif command.startswith("drop "): 
            item_name = command[5:].lower() #Gets the information after the word "drop "
            player.drop_item(item_name) #Gets the player to drop the item

        elif command == "inventory":
            if player.inventory:
                print("You have:")
                for item in player.inventory: #Checks inventory
                    print(f" - {item.get_name()} (\"{item.get_short_name()}\")") #Prints each item with full name and short name
                print(f"Total weight: {player.get_current_weight()} kg / {player.max_weight} kg") #Show weight carried vs max weight
            else:
                print("Your inventory is empty.") #Will print if you carry nothing

        elif command.startswith("use "):
            item_name = command[4:].lower() #Gets the item after "use "
            player.use_item(item_name) #Uses the item calles the specific item use method

        elif command == "health":
            print(f"Your health: {player.get_health()}") #Checks the players health

        elif command == "help":
            print_help() #Prints the command log

        else:
            print("I don't understand that command. Type 'help' for a list of commands.") #Prints if you mistype a command 

main() #Runs the main game loop immediately