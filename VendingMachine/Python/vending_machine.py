from threading import Lock
from inventory import Inventory
from product import Product
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from return_change_state import ReturnChangeState
from vending_machine_state import VendingMachineState
from coin import Coin
from note import Note


class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):
            self.inventory = Inventory()
            self.selected_product = None
            self.idle_state = IdleState(self)
            self.ready_state = ReadyState(self)
            self.dispense_state = DispenseState(self)
            self.return_change_state = ReturnChangeState(self)
            self.current_state = self.idle_state
            self.total_payment = 0.0

    @classmethod
    def get_instance(cls):
        return cls()

    def select_product(self, product: Product):
        self.current_state.select_product(product)

    def insert_coin(self, coin: Coin):
        self.current_state.insert_coin(coin)
    
    def insert_note(self, note: Note):
        self.current_state.insert_note(note)
    
    def dispense_product(self):
        self.current_state.dispense_product()
    
    def return_change(self):
        self.current_state.return_change()
    
    def set_state(self, state: VendingMachineState):
        self.current_state = state

    def add_coin(self, coin):
        self.total_payment += coin.value
    
    def add_note(self, note):
        self.total_payment += note.value

    def reset_payment(self):
        self.total_payment = 0.0
    
    def reset_selected_product(self):
        self.selected_product = None