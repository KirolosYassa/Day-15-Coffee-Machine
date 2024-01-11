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
        insufficient_resources = []
        
        try:
            if MENU[drink]["ingredients"]["water"] > self.resources_water:
                all_is_found = False  
                insufficient_resources.append("water")
        except KeyError:
            pass
        finally:
            pass     
        try:
            if MENU[drink]["ingredients"]["milk"] > self.resources_milk:
                all_is_found = False
                insufficient_resources.append("milk")
        except KeyError:
            pass
        finally:
            pass     
        try:
            if MENU[drink]["ingredients"]["coffee"] > self.resources_coffee:
                all_is_found = False
                insufficient_resources.append("coffee")
        except KeyError:
            pass
        finally:
            pass     
        return all_is_found, insufficient_resources
    
    def calculate_coins(self, quarters, dimes, nickles, pennies):
        return (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    
    def process_coins(self, drink):
        drink_cost = float(MENU[drink]["cost"])
        print("Please insert coins:")
        quarters = float(input("How many quarters: "))
        dimes = float(input("How many dimes: "))
        nickles = float(input("How many nickles: "))
        pennies = float(input("How many pennies: "))
        total_inserted_coins = self.calculate_coins(quarters, dimes, nickles, pennies)
        change = total_inserted_coins - drink_cost
        if total_inserted_coins >= drink_cost:
            return True, change
        return False