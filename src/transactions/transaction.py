class Transaction:
    def __init__(self, sender, reciever, amount, metadata=None):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.metadata = metadata
