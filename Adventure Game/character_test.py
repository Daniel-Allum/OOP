from character import Character

harry = Character('Harry', 'A smelly wumpus')
harry.describe()
harry.set_conversation("Come closer. I can't see you!")
harry.talk()

from character import Enemy
harry = Enemy('Harry','A smelly wumpus')