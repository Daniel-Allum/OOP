class Character:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.max_weight = 10
        self.health = 100
        self.max_health = 100