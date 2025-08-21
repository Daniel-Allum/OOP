class Item:
    def __init__(self, name, description=None, weight=0, value=0, short_name=None):
        self.name = name
        self.description = description
        self.weight = weight
        self.value = value
        self.can_pick_up = True
        self.short_name = short_name if short_name else name.lower().replace(" ", "")

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def get_can_pick_up(self):
        return self.can_pick_up

    def get_short_name(self):
        return self.short_name

    def set_description(self, description):
        self.description = description

    def set_weight(self, weight):
        self.weight = weight

    def set_can_pick_up(self, pickable):
        self.can_pick_up = pickable

    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")
        print(f"Weight: {self.weight}kg")
        if not self.can_pick_up:
            print("You cannot pick this up.")

    def use(self, player):
        print(f"You use the {self.name}, but nothing happens.")


class HealthPotion(Item):
    def __init__(self, name, heal_amount=20, weight=1, description=None, short_name=None):
        super().__init__(name, description=description, weight=weight, short_name=short_name)
        self.heal_amount = heal_amount

    def use(self, player):
        player.health = min(player.max_health, player.health + self.heal_amount)
        print(f"You used {self.name} and restored {self.heal_amount} HP! Your health is now {player.health}.")
        if self in player.inventory:
            player.inventory.remove(self)


class Key(Item):
    def __init__(self, name, unlocks_room_name, description=None, weight=1, value=0, short_name=None):
        super().__init__(name, description, weight, value, short_name)
        self.unlocks = unlocks_room_name
        self.used = False

    def use(self, player):
        if not self.used:
            print(f"You use the {self.name} on the {self.unlocks}.")
            self.used = True
        else:
            print(f"The {self.name} has already been used.")


class Torch(Item):
    def __init__(self, name, description=None, weight=2, value=0, short_name=None):
        super().__init__(name, description, weight, value, short_name)
        self.lit = False

    def use(self, player):
        if self.lit:
            print("You extinguish the torch.")
            self.lit = False
        else:
            print("You light the torch. The room brightens up.")
            self.lit = True


class Weapon(Item):
    def __init__(self, name, description=None, weight=0, value=0, damage=0, weapon_type="Melee", short_name=None):
        super().__init__(name, description, weight, value, short_name)
        self.damage = damage
        self.weapon_type = weapon_type

    def use(self, target):
        print(f"You attack {target} with {self.name}, dealing {self.damage} damage.")

    def get_damage(self):
        return self.damage

    def __str__(self):
        return f"{self.name} (Type: {self.weapon_type}, Damage: {self.damage})"