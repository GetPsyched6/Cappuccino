import unittest
from src.transactions.transaction import Transaction

FIXED_SENDER_PUBLIC_KEY = (
    "f4236da27a6cb1564bc3a8c0ddc1bd36e04733bf289cebe47afbbae4e7d53102"
)
FIXED_RECIEVER_PUBLIC_KEY = (
    "6619cbe600096e3c88595e4ed82ced1d0375dc1f5c5c1270f9484c3414383560"
)

FIXED_TEST_TIMESTAMP = 1710421770.8


class TestTransaction(unittest.TestCase):
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

    def test_transaction_str(self):
        self.assertIsInstance(
            str(self.tx1),
            str,
            "The transaction string function should return type string",
        )


if __name__ == "__main__":
    unittest.main()
