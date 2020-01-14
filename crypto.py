from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import os

# *** Encryption Functions ***
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

# *** Decryption Functions ***
def decrypt(encrypted_text, key):
    initialization = encrypted_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, initialization)
    plaintext = cipher.decrypt(encrypted_text[AES.block_size:])
    return plaintext.rstrip(b"\0")

def file_decrypt(file_name, key):
    with open(file_name, 'rb') as input_file:
        encrypted_text = input_file.read()
    decrypted_text = decrypt(encrypted_text, key)
    with open(file_name[:-4], 'wb') as output_file:
        output_file.write(decrypted_text)
    os.remove(file_name)

# This function takes an alphanumeric string as a password and passes it to pycryptodome's PBKDF2 
# algorithm to generate an encryption key 
def generate_key(password):
    salt = b'\x83\xdb\xb9\xd3\xdc"\x1e\x0ee"\x0c\xf0=5\xab_\x18\xd7\xd2\x98\x92Q.\xbd\x9cK\x96\x93-J\x08\xe0'
    return PBKDF2(password, salt, dkLen=32)

secretfile = "top_secret.txt"

password = str(input("Enter a password for encryption:"))
key = generate_key(password)

option = int(input("Enter 1 to encrypt file.\nEnter 2 to decrypt file.\nSelection:"))
if option == 1:
    file_encrypt(secretfile, key)
    print("file encrypted!")

elif option == 2:
    encrypted = secretfile + ".enc"
    file_decrypt(encrypted, key)
    print("file decrypted!")
