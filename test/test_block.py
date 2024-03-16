import unittest
from src.blockchain.block import Block
from src.transactions.transaction import Transaction

FIXED_SENDER_PUBLIC_KEY = (
    "f4236da27a6cb1564bc3a8c0ddc1bd36e04733bf289cebe47afbbae4e7d53102"
)
FIXED_RECIEVER_PUBLIC_KEY = (
    "6619cbe600096e3c88595e4ed82ced1d0375dc1f5c5c1270f9484c3414383560"
)
FIXED_EXPECTED_HASH = "b38ebad6a651cc3b6943ccb6cff0aff12f13de429d9dca0328326fcb1b5bda4d"

FIXED_TEST_TIMESTAMP = 1710421770.8


class TestBlock(unittest.TestCase):

    tx1 = Transaction(
        FIXED_SENDER_PUBLIC_KEY,
        FIXED_RECIEVER_PUBLIC_KEY,
        _test_timestamp=FIXED_TEST_TIMESTAMP,
        amount=1,
    )
    tx2 = Transaction(
        FIXED_SENDER_PUBLIC_KEY,
        FIXED_RECIEVER_PUBLIC_KEY,
        _test_timestamp=FIXED_TEST_TIMESTAMP,
        amount=50,
    )
    transactions = [str(tx1), str(tx2)]

    block = Block(
        index=1,
        transactions=transactions,
        prev_hash="0",
        _test_timestamp=FIXED_TEST_TIMESTAMP,
    )

    def test_block_hashing(self):
        self.assertEqual(
            FIXED_EXPECTED_HASH,
            self.block.compute_hash(),
            "The block hash should match the expected hash",
        )

    def test_block_str(self):
        self.assertIsInstance(
            str(self.block), str, "The block string function should return type string"
        )


if __name__ == "__main__":
    unittest.main()
