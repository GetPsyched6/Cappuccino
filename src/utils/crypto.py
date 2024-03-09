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
