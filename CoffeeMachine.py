from menu import MENU 
from menu import resources 

class CoffeeMachine:
    
    
    def __init__(self):
        self.resources_water = resources["water"]
        self.resources_milk = resources["milk"]
        self.resources_coffee = resources["coffee"]
        self.money = 0
        
    def display_report_of_current_resources(self):
        return f"""
the current resource values:
Water: {self.resources_water}ml
Milk: {self.resources_milk}ml
Coffee: {self.resources_coffee}g
Money: ${self.money}
"""

    def check_resources_sufficients(self, drink):
        all_is_found = True
        
        try:
            if MENU[drink]["ingredients"]["water"] > self.resources_water:
                all_is_found = False  
        except KeyError:
            pass
        finally:
            pass     
        try:
            if MENU[drink]["ingredients"]["milk"] > self.resources_milk:
                all_is_found = False
        except KeyError:
            pass
        finally:
            pass     
        try:
            if MENU[drink]["ingredients"]["coffee"] > self.resources_coffee:
                all_is_found = False
        except KeyError:
            pass
        finally:
            pass     
        return all_is_found