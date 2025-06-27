from vending_machine_state import VendingMachineState
from coin import Coin
from product import Product
from note import Note


class IdleState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine

    def select_product(self, product: Product):
        #Check if the product that is selected is not empty
        if self.vending_machine.inventory.is_available(product):
            self.vending_machine.selected_product = product
            self.vending_machine.set_state(self.vending_machine.ready_state)
            print(f" Product selected: {product.name}")
        else:
            print(f"Product is not available {product.name}. Select a different product")
    
    def insert_coin(self, coin: Coin):
        print("Select the Product first")
    
    def insert_note(self, note: Note):
        print("Select the Product first")

    def return_change(self):
        print("No change to return")
    
    def dispense_product(self):
        print("Select the Product first")