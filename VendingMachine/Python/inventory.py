class Inventory:
    def __init__(self) -> None:
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = quantity
    
    def remove_product(self, product):
        del self.products[product]

    def update_quantity(self, product, quantity):
        self.products[product] = quantity
    
    def get_quantity(self, product):
        return self.products[product]
    
    def is_available(self, product):
        return product in self.products and self.products[product] > 0
    
