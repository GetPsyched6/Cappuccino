from ecdsa import SigningKey, SECP256k1
import hashlib


def hash_data(data):
    """
    Generates a SHA-256 hash of the given data.

    :param data: string representation of the data
    :return: Hex string representing hash of data
    """

    data_string = str(data).encode()
    hash_object = hashlib.sha256(data_string)
    return hash_object.hexdigest()


def generate_ecc_keys():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.verifying_key

    private_key_str = private_key.to_string().hex()
    public_key_str = public_key.to_string().hex()

    return private_key_str, public_key_str


def sign_data(data, sender_private_key):
    return sender_private_key.sign(str.encode(str(data)))


def verify_signature(data, signature, sender_public_key):
    return sender_public_key.verify(signature, str.encode(str(data)))
