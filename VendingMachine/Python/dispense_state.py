from vending_machine_state import VendingMachineState
from note import Note
from coin import Coin
from product import Product 

class DispenseState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine
    
    def select_product(self, product: Product):
        print("Product already selected. It's ready to get dispensed")

    def insert_coin(self, coin: Coin):
        print("Payment Already made")
    
    def insert_note(self, note: Note):
        print("Payment Already made")

    def dispense_product(self):
        print("Started dispensing the product")
        product = self.vending_machine.selected_product
        quantity = self.vending_machine.inventory.get_quantity(product)
        self.vending_machine.inventory.update_quantity(product, quantity-1)
        print(f"Product Dispensed {product.name}")
        self.vending_machine.set_state(self.vending_machine.return_change_state)

    def return_change(self):
        print("Collect the product first")