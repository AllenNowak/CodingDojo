class Fighter:
    def __init__(self):
        self.name = "Default Character Name"
        self.health = 100
        self.strength = 10
        self.agility = 5
        self.defense = 3
        self.special = "not implemented"

    def attack(self, target):
        target.defend(self.strength)
        print(f'{self.name} is attacking {target.name}')

    def defend(self, amount):
        damage = amount - self.defense
        self.health -= damage
        print(f'{self.name} took {damage} and now has {self.health} health')

    def use_special(self):
        raise NotImplementedError
    def use_buff(self):
        raise NotImplementedError
    
