from product import Product
from store import Store


warehouse = Store('MassiveMart')
inventory = [
    Product('waffles', 1.0, 'frozen'),
    Product('pizza', 7.0, 'frozen'),
    Product('ice cream', 2.0, 'frozen'),
    Product('pot pies', 3.0, 'frozen'),
    Product('choco tacos', 4.0, 'frozen'),
    Product('peas', 1.0, 'frozen'),
    Product('carrots', 1.0, 'frozen'),
    Product('potatoes', 2.0, 'vegetables'),
    Product('asparagus', 3.0, 'vegetables'),
    Product('lettuce', 2.0, 'vegetables'),
    Product('green beans', 2.0, 'vegetables'),
    Product('yellow corn', 1.0, 'vegetables'),
    Product('peas', 1.0, 'vegetables'),
    Product('carrots', 1.0, 'vegetables')
]

for inv in inventory:
    warehouse.add_product(inv)

print('Some Products:')
print('# 1', inventory[0])
print('# 2', inventory[1])
print('# 3', inventory[2])
print('# 4', inventory[3])
print('# 14', inventory[13])

print('Warehouse contents:')
# print(warehouse)
print('Before Sales:')
print(f'# of items in inventory - {len(warehouse.products)}, first is: {warehouse.products[0]}')
print(f'First item in inventory - {warehouse.products[0]}')
warehouse.sell_product(0)
warehouse.sell_product(0)
warehouse.sell_product(0)
print('After Sales:')
print(f'# of items in inventory - {len(warehouse.products)}, first is: {warehouse.products[0]}')
print(f'First item in inventory - {warehouse.products[0]}')

# NINJA BONUS: Add the inflation method to the Store class
inv_size = len(warehouse.products)
print('\nBefore inflation...')
print(f'the price of fresh carrots is {warehouse.products[inv_size - 1]}')
print(f'the price of fresh green beans is {warehouse.products[inv_size - 4]}')
warehouse.inflation(25)
print('\nAfter inflation...')
print(f'the price of fresh carrots is {warehouse.products[inv_size - 1]}')
print(f'the price of fresh green beans is {warehouse.products[inv_size - 4]}')


# NINJA BONUS: Add the set_clearance method to the Store class
category = 'vegetables'
print('\nBefore clearance, the veggie inventory is:')
veggies = [i for i in warehouse.products if i.category == category]
for veg in veggies:
    print(veg)

warehouse.set_clearance(category, 50)
print('\nAfter clearance, the veggie inventory is:')
veggies = [i for i in warehouse.products if i.category == category]
for veg in veggies:
    print(veg)

# SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.
warehouse = Store('KwikStop')
inventory = [
    Product('nachos',   2.0, 'snacks'),
    Product('pretzels', 2.0, 'snacks'),
    Product('peanuts',  2.0, 'snacks'),
    Product('candy',    2.0, 'snacks'),
    Product('cookies',  2.0, 'snacks'),
]


