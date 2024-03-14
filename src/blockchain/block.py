from ..utils.crypto import hash_data
import time


class Block:
    """ """

    def __init__(self, index, transactions, prev_hash, _test_timestamp=None):
        self.index = index
        self._timestamp = (
            _test_timestamp if _test_timestamp is not None else time.time()
        )
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.nonce = 0

    @property
    def timestamp(self):
        return self._timestamp

    def compute_hash(self):
        block_string = str(self)
        return hash_data(block_string)

    def __str__(self):
        transactions_string = "".join([str(tx) for tx in self.transactions])
        return f"{self.index}{self._timestamp}{transactions_string}{self.prev_hash}{self.nonce}"
