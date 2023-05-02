class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 30
        self.health = 50
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
        print(f'{self.name} says "Graowahw!"')
        return self

class Ninja:
    # implement __init__(first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def __expr__(self):
        return f'First Name - {self.first_name}, Last Name - {self.last_name}, Treats - {self.treats}, Pet Food - {self.pet_food} Pet - {self.Pet} '

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

bonzo = Pet('Bonzo', 'Chimpanzee', 'Insomnia') 
ninja = Ninja('Peter', 'Boyd', 'bananas', 'twigs and leaves', bonzo)

ninja.feed().walk().bathe()


