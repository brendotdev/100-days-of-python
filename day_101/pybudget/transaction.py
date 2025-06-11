from datetime import datetime

class Transaction:
    def __init__(self, amount, category, type):
        self.amount = amount
        self.category = category
        self.type = type  # 'expense' or 'income'
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
            "timestamp": self.timestamp
        }