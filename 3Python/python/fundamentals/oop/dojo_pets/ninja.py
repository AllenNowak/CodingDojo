from pet import Pet

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
        if self.treats > 0:
            self.treats -= 1
        elif self.pet_food > 0:
            self.pet_food -= 1
        else:
            return self
        
        self.pet.eat()
        return self
    
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self
