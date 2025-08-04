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

    def move(self, direction):
        new_room = self.current_room.move(direction)
        if new_room != self.current_room:
            self.current_room = new_room
            print("You move to the " + self.current_room.get_name())
            self.current_room.describe()
        else:
            print("You stay where you are.")

    def get_current_weight(self):
        total_weight = 0
        for item in self.inventory:
            total_weight += item.get_weight()
        return total_weight

    def pick_up(self):
        item = self.current_room.get_item()
        if item is None:
            print("There is nothing here to pick up.")
            return
        if not item.get_can_pick_up():
            print("You can't pick that up.")
            return
        if self.get_current_weight() + item.get_weight() > self.max_weight:
            print("You're overburdened and can't carry that.")
            return
        self.inventory.append(item)
        self.current_room.set_item(None)
        print("You picked up the " + item.get_name())

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.get_name().lower() == item_name.lower():
                self.inventory.remove(item)
                self.current_room.set_item(item)
                print("You dropped the " + item.get_name())
                return
        print("You don't have that item.")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.get_name().lower() == item_name.lower():
                item.use(self)
                return
        print("You don't have that item.")

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print("Your health is now: " + str(self.health))
        