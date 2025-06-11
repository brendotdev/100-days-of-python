class Budget:
    def __init__(self, income):
        self.income = income
        self.categories = {}

    def add_category(self, name, amount):
        self.categories[name] = amount

    def update_category(self, name, amount):
        if name in self.categories:
            self.categories[name] += amount
        else:
            self.categories[name] = amount

    def get_summary(self):
        total_spent = sum(self.categories.values())
        return {
            "income": self.income,
            "spent": total_spent,
            "remaining": self.income - total_spent,
            "breakdown": self.categories
        }