class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def __str__(self):
        # https://stackabuse.com/format-number-as-currency-string-in-python/
        return f'Name: {self.name}, Category: {self.category}, Price: ' + '${:,.2f}'.format(self.price)
    def print_info(self):
        print(self)
        return self
    def update_price(self, percent_change, is_increased):
        delta = (100 + percent_change if is_increased else 100 - percent_change) * 0.01
        self.price *= delta
        return self

