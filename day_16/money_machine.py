class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            count = int(input(f"How many {coin}?: "))
            self.money_received += count * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.money_received = 0
        total_inserted = self.process_coins()
        if total_inserted >= cost:
            change = round(total_inserted - cost, 2)
            if change > 0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
