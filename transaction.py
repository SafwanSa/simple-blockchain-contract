import json


class Transaction:

    def __init__(self, from_id, to_id, amount):
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_dict(self):
        return {
            'from_id': self.from_id,
            'to_id': self.to_id,
            'amount': self.amount,
        }
