class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,  # Corrected typo 'nickles' to 'nickels'
        "pennies": 0.01
    }

    def __init__(self):
        """Initialize the MoneyMachine with zero profit and money received."""
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Print the current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Prompts the user to insert coins and
          calculates the total amount received."""
        print("Please insert coins.")
        total = 0
        for coin, value in self.COIN_VALUES.items():
            while True:
                try:
                    coin_count = int(input(f"How many {coin}?: "))
                    if coin_count < 0:
                        raise ValueError("The number of coins cannot be negative.")
                    total += coin_count * value
                    break  # Exit loop if input is valid
                except ValueError as e:
                    print(f"Invalid input. Please enter a positive integer. Error: {e}")
        self.money_received = total
        return total


    def make_payment(self, cost):
        """Accepts payment if sufficient funds are received; returns True if successful."""
        self.money_received = self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0  # Reset money_received after successful payment
            return True
        print("Sorry that's not enough money. Money refunded.")
        self.money_received = 0  # Reset money_received after failure
        return False
