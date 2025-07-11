import time
import sys
import os
from cryptography.fernet import Fernet
from tqdm import tqdm
from colorama import init, Fore, Style
from pyfiglet import Figlet

init(autoreset=True)

# === Styled Headers ===
def print_header():
    f = Figlet(font='slant')
    print(Fore.RED + f.renderText('Image Cryptography'))
    print(Fore.LIGHTBLUE_EX + "🔐 Secure Image Encryption & Decryption Utility")
    print(Fore.BLUE + "-" * 60)

# === Animation Progress Bar ===
def show_animation(action="Encrypting"):
    print(Fore.YELLOW + f"\n{action} Image...")
    for _ in tqdm(range(50), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.01)
    print(Fore.GREEN + f"{action} complete!\n")

# === Key Generation ===
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print(Fore.GREEN + "\n[🗝️] Key generated and saved as 'secret.key'!\n")

# === Load Key ===
def load_key():
    if not os.path.exists("secret.key"):
        print(Fore.RED + "❌ No key found. Please generate it first (Option 1).")
        sys.exit()
    return open("secret.key", "rb").read()

# === Encrypt Image ===
def encrypt_image(image_path, encrypted_path):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(image_path, "rb") as file:
            original_data = file.read()
    except FileNotFoundError:
        print(Fore.RED + f"❌ '{image_path}' not found.")
        return

    show_animation("Encrypting")
    encrypted_data = fernet.encrypt(original_data)

    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)

    print(Fore.GREEN + f"[🔐] Encrypted image saved as: {encrypted_path}\n")

# === Decrypt Image ===
def decrypt_image(encrypted_path, decrypted_path):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(encrypted_path, "rb") as file:
            encrypted_data = file.read()
    except FileNotFoundError:
        print(Fore.RED + f"❌ '{encrypted_path}' not found.")
        return

    try:
        show_animation("Decrypting")
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception:
        print(Fore.RED + "❌ Decryption failed. Possible causes:")
        print("- Wrong key")
        print("- Corrupt encrypted file")
        print("- Key mismatch (re-generated?)")
        return

    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)

    print(Fore.GREEN + f"[🔓] Decrypted image saved as: {decrypted_path}\n")

# === Main Menu ===
def main_menu():
    while True:
        print_header()
        print(Fore.LIGHTCYAN_EX + "📋 Choose an option:")
        print(Fore.LIGHTWHITE_EX + "  [1] Generate Encryption Key")
        print("  [2] Encrypt Image")
        print("  [3] Decrypt Image")
        print("  [4] Exit")
        print(Fore.BLUE + "-" * 60)

        choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice (1/2/3/4): ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            encrypt_image("original_image.jpg", "encrypted_image.bin")
        elif choice == '3':
            decrypt_image("encrypted_image.bin", "decrypted_image.jpg")
        elif choice == '4':
            print(Fore.CYAN + "\n👋 Exiting ImgCrypt. Stay secure!")
            break
        else:
            print(Fore.RED + "❌ Invalid input. Please choose 1, 2, 3 or 4.")

        input(Fore.LIGHTBLACK_EX + "\n[Press Enter to continue...]")
        os.system('cls' if os.name == 'nt' else 'clear')


# === Launch ===
if __name__ == "__main__":
    main_menu()
