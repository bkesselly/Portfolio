import base64
import hashlib
import random
import string
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# function to generate a random password
def generate_password():
    # choose 12 random characters from the set of lowercase letters and digits
    password = "".join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return password

# generate a random password
password = generate_password()
print("Generated password:", password)

# prompt the user to decide whether to encrypt the password or not
choice = input("Do you want to encrypt the password? (y/n) ")

if choice.lower() == "y":
    # create a salt
    salt = b"this is a salt"

    # use PBKDF2 to derive a secure key from the password and salt
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000, dklen=32)

    # create a cipher object using the key
    cipher = AES.new(key, AES.MODE_EAX)

    # encrypt the password
    ciphertext, tag = cipher.encrypt_and_digest(password.encode("utf-8"))

    # encode the encrypted password and tag as base64
    encoded_ciphertext = base64.b64encode(ciphertext).decode("utf-8")

    # print the encrypted password
    print("Encrypted password:", encoded_ciphertext)
else:
    print("Exiting program.")
