from product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def __repr__(self):
        rep = f'Name: {self.name}\n'
        for prod in self.products:
            # https://stackabuse.com/format-number-as-currency-string-in-python/
            rep += f"Product: {prod.name} @ "
            rep += "${:,.2f}".format(prod.price) + "\n"
        return rep
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, id):
        product = self.products.pop(id)
        product.print_info()
        return self
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_discount):
        clearance_list = [pr for pr in self.products if pr.category == category]
        for product in clearance_list:
            product.update_price(percent_discount, False)
        return self



