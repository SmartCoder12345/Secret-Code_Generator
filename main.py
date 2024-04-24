"""
Project Name - Secret-Code Generator
Author: #Smart_Coder
"""

import customtkinter as ctk
import tkinter.messagebox as tmsg
import pyperclip
from cryptography.fernet import Fernet

# Set appearance mode to dark and default color theme to dark-blue
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def encrypt(message: str) -> str:
    """
    This function encrypts the given message.
    :param message: Message to be encrypted.
    :return: Encrypted Message
    """
    message = message.encode()
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message)
    encrypted_message += b"|" + key

    return encrypted_message.decode()

def decrypt(message: str) -> str | None:
    """
    This function decrypts the given message.
    :param message: Code to be decrypted.
    :return: Decrypted Message
    """
    try:
        message = message.encode()
        encrypted_message, key = message.split(b"|")
        cipher = Fernet(key)
        decrypted_message = cipher.decrypt(encrypted_message)
    except Exception:
        return None

    return decrypted_message.decode()

def mess_parser(isToEncrypt: bool, message: str) -> None:
    """
    This function parses the message and performs encrypting or decrypting based on the input.
    :param isToEncrypt: True if to encrypt, False if to decrypt.
    :param message: Message/Code
    """
    if isToEncrypt:
        mess = encrypt(message)
    else:
        mess = decrypt(message)
        if mess is None:
            # Show error message for invalid message
            tmsg.showerror("Secret Code Generator", "Invalid Code !!")
            return None

    # Copy the message to clipboard
    pyperclip.copy(mess)
    # Show confirmation message
    tmsg.showinfo("Secret Code Generator", f"Your Message/Code has been copied.")

def show_mess(isShow: bool, entry: ctk.CTkEntry) -> None:
    """
    Function to toggle message visibility in the entry box.
    """
    if isShow:
        entry.configure(show="")
    else:
        entry.configure(show="*")

def main():
    # Setting up the main window
    root = ctk.CTk()
    root.title("Secret-Code Generator")
    root.geometry("370x400")
    root.resizable(False, False)
    root.iconbitmap("asset/icon.ico")

    # Label
    label = ctk.CTkLabel(root, text="Secret-Code Generator", font=("Helvetica", 28))
    label.pack(pady=20, padx=10)

    # Entry Box
    entry = ctk.CTkEntry(root, width=200, height=50, placeholder_text="Enter Your Message/Code Here...", font=("Arial", 20), show="*")
    entry.pack(pady=20, fill="x", padx=20)

    # Checkbox
    show_pass = ctk.BooleanVar()
    my_check = ctk.CTkCheckBox(root, text="Show Message/Code", variable=show_pass, onvalue=True, offvalue=False, command=lambda: show_mess(show_pass.get(), entry))
    my_check.pack(pady=15)

    # Button to code the message
    code_butt = ctk.CTkButton(root, text="Encrypt Message", height=50, font=("Helvetica", 20), command=lambda: mess_parser(True, entry.get()))
    code_butt.pack(pady=10, fill="x", padx=10)

    # Button to decode the message
    code_butt = ctk.CTkButton(root, text="Decrypt Code", height=50, font=("Helvetica", 20), command=lambda: mess_parser(False, entry.get()))
    code_butt.pack(pady=20, fill="x", padx=10)

    root.mainloop()

if __name__ == '__main__':
    main()