from Crypto.Cypher import AES
from Crypto.Protocol.KDF import PBKDF2

# This function takes an alphanumeric string as a password and passes it to pycryptodome's PBKDF2 
# algorithm to generate an encryption key 
def generate_key(password):
    salt = b'\x83\xdb\xb9\xd3\xdc"\x1e\x0ee"\x0c\xf0=5\xab_\x18\xd7\xd2\x98\x92Q.\xbd\x9cK\x96\x93-J\x08\xe0'
    return PBKDF2(password, salt, dkLen=32)


