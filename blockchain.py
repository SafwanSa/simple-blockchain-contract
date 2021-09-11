import json
from block import Block
import copy
from transaction import Transaction


class BlockChain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 100
        self.difficulty = 2

    def create_genesis_block(self):
        genesis = Block([Transaction(None, None, 0)], 'hash')
        genesis.hash = genesis.calculate_hash()
        return genesis

    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_reward_id):
        block = Block(self.pending_transactions)
        block.previous_hash = self.get_last_block().hash
        block.mine_block(self.difficulty)

        print('Block successfully mined!')
        self.chain.append(block)

        self.pending_transactions = [
            Transaction(None, miner_reward_id, self.mining_reward)
        ]

    def add_transaction(self, transaction):
        if not transaction.from_id or not transaction.to_id:
            raise Exception('Transaction must include from and to ids.')


        if not transaction.is_valid():
            raise Exception('Cannot add invalid transaction to the block.')

        self.pending_transactions.append(transaction)

    def get_balance_of_id(self, id):
        balance = 0.0
        for block in self.chain:
            for transaction in block.transactions:
                if id == transaction.from_id:
                    balance -= transaction.amount

                if id == transaction.to_id:
                    balance += transaction.amount

        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if not current_block.has_valid_transactions():
                return False

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        blocks = []
        for block in self.chain:
            blocks.append(block.to_dict())

        return json.dumps(blocks, indent=4)
