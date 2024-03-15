import json


class Transaction:
    def __init__(self, sender, receiver, amount, metadata=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.metadata = metadata

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "metadata": self.metadata,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True)
    
