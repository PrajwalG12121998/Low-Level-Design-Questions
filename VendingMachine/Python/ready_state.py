from vending_machine_state import VendingMachineState
from product import Product
from note import Note
from coin import Coin

class ReadyState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine

    def select_product(self, product: Product):
        print("Product is already selected. Please make a payment")

    def insert_coin(self, coin: Coin):
        self.vending_machine.add_coin(coin)
        print(f"Coin added successfully {coin.value}")
        self.check_payment_status()
    
    def insert_note(self, note: Note):
        self.vending_machine.add_note(note)
        print(f"Note added succesfully {note.value}")
        self.check_payment_status()
    
    def dispense_product(self):
        print("Please make payment first")
    
    def return_change(self):
        print("Change will be returned after the product is dispensed")

    def check_payment_status(self):
        if self.vending_machine.total_payment >= self.vending_machine.selected_product.price:
            self.vending_machine.set_state(self.vending_machine.dispense_state)

    