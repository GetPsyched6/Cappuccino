from ..utils.crypto import hash_data
import time
import json


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

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self._timestamp,
            "transactions": self.transactions,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce,
        }

    def __str__(self):
        transactions_string = "".join([str(tx) for tx in self.transactions])
        block_dict = self.to_dict()
        block_dict["transactions"] = transactions_string
        return json.dumps(block_dict, sort_keys=True)
