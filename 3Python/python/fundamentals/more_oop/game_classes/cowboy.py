from game_classes.fighter import Fighter

class Cowboy(Fighter):
    def __init__(self):
        super().__init__()
        self.buff = "YeeHaw"
        self.special = "Six Shooter"
    def use_special(self, target):
        chance = random.randint(1,2)
        if chance > 1:
            print(f'Lucky hit! {self.name} fires twice!')
            target.defend(10)
            target.defend(10)
        else:
            print(f'{self.name} fires once')
            target.defend(10)
    def use_buff(self):
        print(f'{self.name} screams YEEHAWWW!')
        self.strength += 3
        print(f"{self.name} is fired up, strength up by 3, it's now {self.strength}")

