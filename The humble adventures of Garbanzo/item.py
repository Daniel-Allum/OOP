class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.weight = 0
        self.can_pick_up = True

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def set_weight(self, item_weight):
        self.weight = item_weight

    def get_weight(self):
        return self.weight

    def set_can_pick_up(self, pickable):
        self.can_pick_up = pickable

    def get_can_pick_up(self):
        return self.can_pick_up

    def describe(self):
        print("The [" + self.name + "] is here - " + self.description)
        print("Weight: " + str(self.weight) + "kg")
        if not self.can_pick_up:
            print("You cannot pick this up.")

    def use(self, player):
        print("You use the " + self.name + ", but nothing happens.")


class HealthPotion(Item):
    def __init__(self, item_name):
        super().__init__(item_name)

    def use(self, player):
        print("You drink the " + self.name + ". You feel refreshed!")
        player.heal(20)
        player.inventory.remove(self)


class Key(Item):
    def __init__(self, item_name, unlocks_room_name):
        super().__init__(item_name)
        self.unlocks = unlocks_room_name

    def use(self, player):
        print("You try using the " + self.name + " on the " + self.unlocks + ".")


class Torch(Item):
    def __init__(self, item_name):
        super().__init__(item_name)
        self.lit = False

    def use(self, player):
        if self.lit:
            print("You extinguish the torch.")
            self.lit = False
        else:
            print("You light the torch. The room brightens up.")
            self.lit = True

class Weapon(Item):
    def __init__(self, name, description, weight, value, damage, weapon_type):
        super().__init__(name, description, weight, value)
        self.damage = damage
        self.weapon_type = weapon_type

    def use(self, target):
        print(f"You attack {target} with {self.name}, dealing {self.damage} damage.")

    def __str__(self):
        base = super().__str__()
        return f"{base} | Type: {self.weapon_type} | Damage: {self.damage}"