import hashlib
from blockchain import BlockChain
from block import Block
from transaction import Transaction


ch = BlockChain()

ch.create_transaction(Transaction('address1', 'address2', 100))
ch.create_transaction(Transaction('address2', 'address1', 50))
ch.create_transaction(Transaction('address5', 'address6', 50))

print('Starting a miner.')
ch.mine_pending_transactions('safwan')
print("Safwan's balance: {}".format(ch.get_balance_of_id('safwan')))


print('Starting a miner again.')
ch.mine_pending_transactions('safwan')
print("Safwan's balance: {}".format(ch.get_balance_of_id('safwan')))


print(ch)
