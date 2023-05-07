from game_classes.kickboxer import Kickboxer
from game_classes.cowboy import Cowboy

cowboy = Cowboy()
kb = Kickboxer()


print ('Welcome to Cowboy vs Kickboxer, you are the Cowboy')
while cowboy.health >= 0 and kb.health >= 0:
    response = ''
    while response != 1 and response != 2 and response != 3:
        response = input('Choose an action\n 1)Attack\n 2)Use Special\n 3)Use Buff')
        
