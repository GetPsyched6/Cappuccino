schema_transaction = {
    "title": "transaction",
    "type": "object",
    "properties": {
        "sender": {"type": "string"},
        "receiver": {"type": "string"},
        "amount": {"type": "number"},
        "timestamp": {"type": "number"},
        "signature": {"type": "string"},
        "metadata": {"type": "string"},
    },
    "required": ["sender", "receiver", "amount", "timestamp"],
}
