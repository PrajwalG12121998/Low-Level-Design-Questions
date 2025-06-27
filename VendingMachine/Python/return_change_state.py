from vending_machine_state import VendingMachineState
from coin import Coin
from note import Note
from product import Product

class ReturnChangeState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        super().__init__(vending_machine)
    
    def select_product(self, product: Product):
        print("Product is already selected. Collect the changet")

    def insert_coin(self, coin: Coin):
        print("Please collect the change first")
    
    def insert_note(self, note: Note):
        print("Please collect the note first")
    
    def dispense_product(self):
        print("Product Already dispensed. Collect the change")
    
    def return_change(self):
        selected_product = self.vending_machine.selected_product
        change = self.vending_machine.total_payment - selected_product.price
        if change > 0:
            print(f" Change Returned ${change:.2f}")
        else:
            print("No change to return")
        
        self.vending_machine.reset_payment()
        self.vending_machine.reset_selected_product()
        self.vending_machine.set_state(self.vending_machine.idle_state)