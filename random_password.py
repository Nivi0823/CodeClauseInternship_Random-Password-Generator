import random
import string
import tkinter as tk
import pyperclip


def generate_custom_password(length):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    special_chars = '$_@#'
    digits = string.digits

    # Ensure that each character set is used at least once
    password = (
            random.choice(uppercase_letters) +
            random.choice(lowercase_letters) +
            random.choice(special_chars) +
            random.choice(digits)
    )

    # Fill the remaining characters with a mix of character sets
    remaining_length = length - 4
    all_characters = uppercase_letters + lowercase_letters + special_chars + digits
    password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the password to randomize the order of characters
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length < 4:
            result_label.config(text="Password length must be at least 4 characters.")
        else:
            password = generate_custom_password(password_length)
            result_label.config(text=f"Generated Password: {password}")
            copy_button.config(state="normal")  # Enable the "Copy to Clipboard" button
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number for the password length.")


def copy_to_clipboard():
    generated_password = result_label.cget("text")
    pyperclip.copy(generated_password)


# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Create and place widgets
length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=10)
# Start the GUI event loop
window.mainloop()
