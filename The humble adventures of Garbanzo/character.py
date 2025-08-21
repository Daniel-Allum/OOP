class Character:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.max_weight = 10
        self.health = 100
        self.max_health = 100

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_inventory(self):
        return self.inventory

    def get_current_room(self):
        return self.current_room

    def display_current_room(self):
        """Print the current room's description, items, characters, and exits (with 'out' in Foyer)."""
        print(f"You are in the {self.current_room.get_name()}")
        print(self.current_room.get_description())
        items_in_room = self.current_room.get_items()
        if items_in_room:
            for item in items_in_room:
                item.describe()
        if self.current_room.get_character():
            print(f"You see {self.current_room.get_character().get_name()} here.")
        exits = list(self.current_room.linked_rooms.keys())
        if self.current_room.get_name() == "Foyer" and "out" not in exits:
            exits.append("out")
        print(f"Exits: {', '.join(exits)}")

    def move(self, direction):
        new_room = self.current_room.move(direction)
        if new_room != self.current_room:
            self.current_room = new_room
            print(f"You move to the {self.current_room.get_name()}")
            self.display_current_room()
        else:
            print("You can't go that way.")
            print("You stay where you are.")

    def get_current_weight(self):
        return sum(item.get_weight() for item in self.inventory)

    def pick_up(self):
        items_in_room = self.current_room.get_items()
        if not items_in_room:
            print("There is nothing here to pick up.")
            return
        item = items_in_room[0]
        if not item.get_can_pick_up():
            print("You can't pick that up.")
            return
        if self.get_current_weight() + item.get_weight() > self.max_weight:
            print("You're overburdened and can't carry that.")
            return
        self.inventory.append(item)
        self.current_room.remove_item(item)
        print(f"You picked up the {item.get_name()}")

    def drop_item(self, item_short_name):
        for item in self.inventory:
            if item.get_short_name() == item_short_name.lower():
                self.inventory.remove(item)
                self.current_room.add_item(item)
                print(f"You dropped the {item.get_name()}")
                return
        print("You don't have that item.")

    def use_item(self, item_short_name):
        for item in self.inventory:
            if item.get_short_name() == item_short_name.lower():
                item.use(self)
                return
        print("You don't have that item.")

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"Your health is now: {self.health}")


class NPC(Character):
    def __init__(self, name, starting_room, dialogue=None):
        super().__init__(name, starting_room)
        self.dialogue = dialogue or "Hello!"

    def talk(self):
        print(f"{self.name} says: {self.dialogue}")
        if self.name.lower() == "luther":
            print("Hint: The three keys you need to escape are hidden in the Bedroom, Study, and Library.")


class Enemy(Character):
    def __init__(self, name, starting_room, health=50, damage=5, drop_item=None):
        super().__init__(name, starting_room)
        self.health = health
        self.damage = damage
        self.drop_item = drop_item

    def attack(self, target):
        if isinstance(target, Character):
            print(f"{self.name} attacks {target.get_name()} for {self.damage} damage!")
            target.health -= self.damage
            if target.health < 0:
                target.health = 0
        else:
            print(f"{self.name} tries to attack, but there's nothing to hit.")

    def on_defeat(self):
        if self.drop_item:
            print(f"{self.name} dropped {self.drop_item.get_name()}!")
            self.current_room.add_item(self.drop_item)