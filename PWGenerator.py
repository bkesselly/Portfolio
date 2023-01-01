import tkinter as tk
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
#print("Generated password:", password)

# create the main window
window = tk.Tk()
window.title("Password Generator")

# set window size
window.geometry("400x400")

#set window color
window.configure(bg='#7851a9')

# create a label to display the password
password_label = tk.Label(window, text=password)

# create a function to close the window
def close_window():
  window.destroy()

# create a function to encrypt the password
def encrypt_password():
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

    # update the password label with the encrypted password
    password_label.configure(text=encoded_ciphertext)

# create a button to close the window
close_button = tk.Button(window, text="Close", command=window.destroy)
close_button.pack(pady=20)

# create a button to encrypt the password
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_password)

# place the widgets in the window
password_label.pack()
encrypt_button.pack()


# run the Tkinter event loop
window.mainloop()
