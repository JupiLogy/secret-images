from stegano import lsb
from encrypt import Encrypt, Decrypt

""" Changenotes:
        - some variables were renamed to match python conventions
        - writing of key.key removed, as it is unnecessary and leaves a trace on the machine
"""

def write_to_file():
    key = input("Password for encryption: ")
    in_path = input("Filepath for unencrypted image: ")
    msg_path = input("Filepath to message to write into image: ")
    out_path = input("Filepath to write encrypted image: ")

    cipher_text = Encrypt(msg_path, key)
    encrypted_image = lsb.hide(in_path, cipher_text)
    encrypted_image.save(out_path)

def read_from_file():
    key = input("Password for decryption: ")
    in_path = input("Filepath of encrypted image: ")

    cipher_text = lsb.reveal(in_path)
    plain_text = Decrypt(cipher_text, key)
    print(plain_text)

    opt = input("\nWould you like to save this message? (y = yes)\n")
    if opt == "y":
        filename = input("Please provide a filename: ")
        writetxt = open(filename, "w")
        writetxt.write(plain_text)
        writetxt.close()
