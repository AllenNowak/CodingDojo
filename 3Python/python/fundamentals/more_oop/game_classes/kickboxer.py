# from game_classes import fighter
# pulls in the whole file, req's using fighter.Fighter to reference
from game_classes.fighter import Fighter
# pulls just the Figher class from the fighter module (file or dir)

class Kickboxer(Fighter):
    def __init__(self):
        super().__init__()
        self.name = "Van Damme"
        self.agility += 8
        self.special = "The Splits"
        self.buff = "Defensive Stance"
    def use_special(self):
        target.defend(self.agility)
        print("{self.name} does the splits and it's amazing")
    def use_buff(self):
        self.defend += 2
        print(f'{self.name} uses {self.buff}')

