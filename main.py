import hashlib
from blockchain import BlockChain
from transaction import Transaction
import ed25519


my_key = ed25519.SigningKey(b'fc0bb74ac434fc3e3eafdc76f23ee79953a78a4b0a94a11e8a6d72da8a6b4d8b', encoding='hex')
my_wallet_id = my_key.get_verifying_key().to_ascii(encoding='hex')

ch = BlockChain()

ts1 = Transaction(my_wallet_id, b'address2', 10)
ts1.sign_transaction(my_key)
ch.add_transaction(ts1)

print('Is valid chain?', ch.is_chain_valid())

print('Starting a miner.')
ch.mine_pending_transactions(my_wallet_id)
print("Safwan's balance: {}".format(ch.get_balance_of_id(my_wallet_id)))

ch.chain[1].transactions[0].amount = 1

print('Starting a miner.')
ch.mine_pending_transactions(my_wallet_id)
print("Safwan's balance: {}".format(ch.get_balance_of_id(my_wallet_id)))


print('Is valid chain?', ch.is_chain_valid())

# print(ch)