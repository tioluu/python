from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_input = input("Good morning, what would you like? (espresso/latte/cappuccino): ")
print(f"The user's input is {user_input}")

def coffee_machine():
    is_on = True

    while is_on:
        # Display the menu and prompt the user for their choice
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            is_on = False  # Stop the loop and turn off the machine
        elif choice == "report":
            # Print resource and money reports
            coffee_maker.report()
            money_machine.report()
        else:
            # Check if the choice is a valid menu item
            drink = menu.find_drink(choice)
            if drink:
                # Check if there are enough resources to make the drink
                if coffee_maker.is_resource_sufficient(drink):
                    # Check if the user has inserted enough money
                    if money_machine.make_payment(drink.cost):
                        # Make the drink
                        coffee_maker.make_coffee(drink)
            else:
                print(f"'{choice}' is not a valid option. Please choose again.")

# Run the coffee machine
coffee_machine()
