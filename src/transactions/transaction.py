import time
import json
from jsonschema import validate, ValidationError
from ..utils.crypto import sign_data, verify_signature
from schemas.schema_transaction import schema_transaction


class Transaction:
    def __init__(
        self,
        sender,
        receiver,
        amount,
        signature=None,
        _test_timestamp=None,
        metadata=None,
    ):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self._timestamp = (
            _test_timestamp if _test_timestamp is not None else time.time()
        )
        self.signature = signature
        self.metadata = metadata

    @property
    def timestamp(self):
        return self._timestamp

    @staticmethod
    def from_json(transaction_data):
        data = json.loads(transaction_data)
        return Transaction(**data)

    def sign(self, sender_private_key):
        self.signature = sign_data(self, sender_private_key)

    # TODO: Add more validations
    def is_valid(self):
        transaction_data = self.to_dict()
        try:
            validate(instance=transaction_data, schema=schema_transaction)

            if transaction_data["amount"] <= 0:
                return False
            if not transaction_data["signature"]:
                return False
            return verify_signature(
                transaction_data,
                signature=transaction_data["signature"],
                sender_public_key=transaction_data["sender"],
            )

        except ValidationError as e:
            print(f"Transaction format is invalid: {e.message}")
            return False

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self._timestamp,
            "signature": self.signature,
            "metadata": self.metadata,
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True)
