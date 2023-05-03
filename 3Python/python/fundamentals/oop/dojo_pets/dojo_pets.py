from pet import *
from ninja import Ninja

print('Peter gets a pet')
bonzo = Pet('Bonzo', 'Chimpanzee', 'Insomnia') 
ninja = Ninja('Peter', 'Boyd', 20, 150, bonzo)
ninja.feed().walk().bathe()
print("Bonzo's info: ", ninja.pet)
print('\nAbandon Bonzo for a new pet\n')

ninja.pet = Pig('Babe', 'Pig', 'politics', 4, 44)
ninja.feed().walk().bathe()
print("Babe's info: ", ninja.pet)
print('\nAbandon Babe for an older pet\n')

ninja.pet = Dinosaur('Rex', 'T-Rex', 'Hunting', 77, 150)
ninja.feed().walk().bathe()
print("Rex's info: ", ninja.pet)
