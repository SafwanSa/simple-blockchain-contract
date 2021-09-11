import json
import hashlib
import ed25519


class Transaction:

    def __init__(self, from_id, to_id, amount):
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.signature = None

    def calculate_hash(self):
        return hashlib.sha224(
            ('{}{}{}'.format(
                self.from_id,
                self.to_id,
                self.amount
            ).encode('utf-8')
            )
        ).hexdigest()

    def sign_transaction(self, signing_key):
        if signing_key.get_verifying_key().to_ascii(encoding='hex') != self.from_id:
            raise Exception('You cannot sign this transaction.')

        tr_hash = self.calculate_hash()
        self.signature = signing_key.sign(bytes(tr_hash,  encoding='utf8'), encoding='hex')


    def is_valid(self):
        if self.from_id == '':
            return True

        if self.signature == '' or not self.signature:
            raise Exception('No signature in this transaction')

        try:
            public_key = ed25519.VerifyingKey(self.from_id, encoding='hex')
            public_key.verify(self.signature, bytes(self.calculate_hash(),  encoding='utf8'), encoding='hex')
            return True
        except:
            print("Invalid signature!")
            return False

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_dict(self):
        return {
            'from_id': self.from_id.decode('utf-8') if self.from_id else None,
            'to_id': self.to_id.decode('utf-8') if self.to_id else None,
            'amount': self.amount,
        }
