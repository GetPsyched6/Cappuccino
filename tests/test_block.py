import unittest
from src.blockchain.block import Block
from src.transactions.transaction import Transaction

FIXED_SENDER_PUBLIC_KEY = (
    "f4236da27a6cb1564bc3a8c0ddc1bd36e04733bf289cebe47afbbae4e7d53102"
)
FIXED_RECIEVER_PUBLIC_KEY = (
    "6619cbe600096e3c88595e4ed82ced1d0375dc1f5c5c1270f9484c3414383560"
)
FIXED_EXPECTED_HASH = "9bef9bb1f298b1eecc6347685ec8a0c2a3a21d6a6b9a593a3ce3795428a94e4d"


class TestBlock(unittest.TestCase):

    def test_block_hashing(self):
        tx1 = Transaction(FIXED_SENDER_PUBLIC_KEY, FIXED_RECIEVER_PUBLIC_KEY, amount=1)
        tx2 = Transaction(FIXED_SENDER_PUBLIC_KEY, FIXED_RECIEVER_PUBLIC_KEY, amount=50)
        transactions = [str(tx1), str(tx2)]

        block = Block(
            index=1,
            transactions=transactions,
            prev_hash="0",
            _test_timestamp=1710421770.8,
        )
        print(block)

        self.assertEqual(
            FIXED_EXPECTED_HASH,
            block.compute_hash(),
            "The block hash should match the expected hash",
        )


if __name__ == "__main__":
    unittest.main()
