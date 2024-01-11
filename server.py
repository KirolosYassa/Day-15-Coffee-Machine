from CoffeeMachine import CoffeeMachine
import os

coffeeMachine = CoffeeMachine()
os.system("cls")

def coffee_machine_app():
    
    user_answer = input("What would you like? (espresso/latte/cappuccino):")
    
    if user_answer == "off":
        return
    
    #TODO: 1. print report
    elif user_answer == "report":
        print(coffeeMachine.display_report_of_current_resources())
     
    #TODO: 2. check resources sufficients?
    elif user_answer == "espresso":
        resources_sufficient = coffeeMachine.check_resources_sufficients("espresso")
    elif user_answer == "latte":
        print(coffeeMachine.check_resources_sufficients("latte"))
    elif user_answer == "cappuccino":
        print(coffeeMachine.check_resources_sufficients("cappuccino"))
        
        
    #TODO: 3. process resources 
    #TODO: 4. check transaction successeful?
    #TODO: 5. make coffee
    
    coffee_machine_app()
    
coffee_machine_app()