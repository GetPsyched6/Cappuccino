from utils.crypto import hash_data
import time


class Block:
    def __init__(self, index, transactions, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.nonce = 0

    def compute_hash(self):
        block_string = self.__str__()
        return hash_data(block_string)

    def __str__(self):
        transactions_string = str([str(tx) for tx in self.transactions])
        return f"{self.index}{self.timestamp}{self.transactions_string}{self.prev_hash}{self.nonce}"
