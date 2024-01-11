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
    elif user_answer == "espresso" or user_answer == "latte" or user_answer == "cappuccino":
        drink = user_answer
        resources_sufficients_status, insufficient_resources =coffeeMachine.check_resources_sufficients(drink)
        if resources_sufficients_status == False:
            if len(insufficient_resources) == 1:
                print(f"Sorry there is not enough {insufficient_resources[0]}.")
            elif len(insufficient_resources) == 2:
                print(f"Sorry there is not enough {insufficient_resources[0]} and {insufficient_resources[1]}.")
            elif len(insufficient_resources) == 3:
                print(f"Sorry there is not enough {insufficient_resources[0]}, {insufficient_resources[1]} and {insufficient_resources[2]}.")
            
            return coffee_machine_app()
        #TODO: 3. process resources
        process_coins_status, change = coffeeMachine.process_coins(drink)
            
        #TODO: 4. check transaction successeful?
        if process_coins_status == False:
            print("Sorry that's not enough money. Money Refunded")
            return coffee_machine_app()
            
        #TODO: 5. make coffee
        print(f"Here is the change: ${round(change, 2)}")
        coffeeMachine.make_drink(drink)
        print(f"Here is your {drink} ☕ Enjoy!")
    
    coffee_machine_app()
    
coffee_machine_app()