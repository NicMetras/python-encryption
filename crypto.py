from Crypto.Cypher import AES
from Crypto.Protocol.KDF import PBKDF2
import os

def encrypt(text, key, key_size = 256):
    pad = lambda s: s + b"\0" * (AES.block_size - len(s) % AES.block_size)
    text = pad(text)
    initialization = Random.new().read(16)
    cipher = AES.new(key, AES.MODE_CBC, initialization)
    return initialization + cipher.encrypt(text)

def file_encrypt(file_name, key):
    with open(file_name, 'rb') as input_file:
        plaintext = input_file.read()
    encrypted_text = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as output_file:
        output_file.write(encrypted_text)
    os.remove(file_name)


# This function takes an alphanumeric string as a password and passes it to pycryptodome's PBKDF2 
# algorithm to generate an encryption key 
def generate_key(password):
    salt = b'\x83\xdb\xb9\xd3\xdc"\x1e\x0ee"\x0c\xf0=5\xab_\x18\xd7\xd2\x98\x92Q.\xbd\x9cK\x96\x93-J\x08\xe0'
    return PBKDF2(password, salt, dkLen=32)


