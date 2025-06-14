#This is a Pizza Topping example for showing decorstor design pattern
#You can refer more by looking into the video of Shreyansh on Youtube

from abc import ABC, abstractmethod

#This is an interface for all Base pizza classes
class Pizza(ABC):
    @abstractmethod
    def get_cost():
        pass

    @abstractmethod
    def description():
        pass

#IS A relationship with pizza
class Margherita(Pizza):
    
    def get_cost(self):
        return 100
    
    def description(self):
        return "Margherita"

#IS-A relationship with pizza
class VegDelight(Pizza):
    def get_cost(self):
        return 120
    
    def description(self):
        return "Veg Delight"

#IS-A relationship with Pizza because it extends that
#  and also has HAS-A relation ship with basically "Margherita has Mushroom toopings"
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza


class Mushrooms(ToppingDecorator):
    def get_cost(self):
        return self.pizza.get_cost() + 10

    def description(self):
        return self.pizza.description() + " Mushrooms"
    
class Cheese(ToppingDecorator):
    def get_cost(self):
        return self.pizza.get_cost() + 15
    
    def description(self):
        return self.pizza.description() + " Cheese"


if __name__ == "__main__":
    pizza = Margherita()
    new_mushroom_pizza = Mushrooms(pizza)

    print("New Mushroom Margherita Pizza cost ", new_mushroom_pizza.get_cost(), new_mushroom_pizza.description())

    new_mush_cheese_pizza = Cheese(new_mushroom_pizza)

    print(new_mush_cheese_pizza.description(), new_mush_cheese_pizza.get_cost())
