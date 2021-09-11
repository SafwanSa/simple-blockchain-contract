import hashlib
import json
from datetime import datetime


class Block:

    def __init__(self, transactions, previous_hash=''):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = datetime.now()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha224(
            ('{}{}{}'.format(
                self.previous_hash,
                json.dumps(self.get_serialized_transactions()),
                self.nonce
            ).encode('utf-8')
            )
        ).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != ''.join(['0' for i in range(difficulty)]):
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(self.hash)

    def has_valid_transactions(self):
        for transaction in self.transactions:
            if not transaction.is_valid():
                return False

        return True

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_dict(self):
        return {
            'hash': self.hash,
            'transactions': self.get_serialized_transactions(),
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'previous_hash': self.previous_hash,
        }

    def get_serialized_transactions(self):
        trs = []
        for i in range(len(self.transactions)):
            trs.append((self.transactions[i]).to_dict())
        return trs
