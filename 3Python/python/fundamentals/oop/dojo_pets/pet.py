class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, energy=30, health=50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
    def __str__(self):
        return f'Name: {self.name}, Type: {self.type}, Energy: {self.energy}, Health: {self.health}'

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f'{self.name} says, "zzzzzz"')
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'{self.name} says, "nom,nom,nom"')
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f'{self.name} plays excitedly')
        return self

    # noise() - prints out the pet's sound    
    def noise(self):
        print(f'{self.name} says "Oink!"')
        return self

class Dinosaur(Pet):
    def __init__(self, name, type, tricks, energy, health, kill_count=0):
        super().__init__(name, type, tricks, energy, health)
        self.kill_count = kill_count
    def __str__(self):
        return super().__str__() + f' Kills: {self.kill_count}'
    def eat(self):
        super().eat()
        self.kill_count += 1
        return self
    def play(self):
        super().play()
        print(f'{self.name} eats carnivorously')
        self.kill_count += 14
        return self
    def noise(self):
        print(f'{self.name} says "RRRR-OOOO-AAA-RRrrrr!"')
        self.kill_count += 1
        return self

class Pig(Pet):
    def __init__(self, name, type, tricks, energy, health, mud_baths=0):
        super().__init__(name, type, tricks, energy, health)
        self.mud_baths = mud_baths
    def __str__(self):
        return super().__str__() + f' Mud Baths: {self.mud_baths}'
    def play(self):
        self.health += 10
        self.mud_baths += 1
        print(f'{self.name} plays excitedly in the mud')
        return self


