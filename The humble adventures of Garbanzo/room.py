class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.items = []

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def remove_character(self):
        self.character = None

    def describe(self):
        print(self.description)
        if self.items:
            for item in self.items:
                item.describe()
        if self.character:
            print("You see " + self.character.get_name() + " here.")
        if self.linked_rooms:
            exits = ", ".join(self.linked_rooms.keys())
            print(f"Exits: {exits}")

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self

    def get_details(self):
        print(self.description)
        print("\nExits:")
        for direction, room in self.linked_rooms.items():
            print(f"The {room.get_name()} is {direction}")