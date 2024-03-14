class Transaction:
    def __init__(self, sender, reciever, amount, metadata=None):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.metadata = metadata

    def __str__(self):
        return f"{self.sender}{self.reciever}{self.amount}{self.metadata}"
