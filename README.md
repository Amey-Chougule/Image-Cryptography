![ImgCrypt Banner](banner.png)
# 🖼️ Image Cryptography 🔐

A terminal-based Python tool to **encrypt and decrypt image files securely** using AES-based Fernet encryption. This project provides a sleek CLI interface with styled output and animations, ideal for cybersecurity learning, Python practice, or real-world encryption needs.

---

## 📌 Project Overview

**Image Cryptography** is a Python CLI tool that:
- Encrypts any image file (e.g. `.jpg`, `.png`) into a secure binary format.
- Decrypts the binary back into its original image format.
- Uses symmetric encryption via the `cryptography.Fernet` module.
- Includes styled terminal output with progress bars and ASCII art banners.

---

## 🚀 Features

- 🔐 **AES-128 encryption (Fernet-based)**
- 🖼️ **Supports `.jpg`, `.png`, `.bmp`, etc.**
- 🎨 **Colorful CLI output** via `colorama` and `pyfiglet`
- 📊 **Progress animations** via `tqdm`
- 🔑 **One-time encryption key generation**
- 🧠 **Beginner-friendly, well-documented**

---

## 📁 Project Structure

image-cryptography/
- ├── main.py # Main Python script
- ├── requirements.txt # Python dependencies
- ├── .gitignore # Files to exclude from Git
- ├── README.md # Project documentation
- ├── LICENSE # Open source license
- ├── secret.key # Encryption key (generated locally)
- ├── original_image.jpg # Input image (not committed)
- ├── encrypted_image.bin # Output (not committed)
- ├── decrypted_image.jpg # Output (not committed)


---
## 🧰 How to Clone and Run the Project
### 1. Clone the repository
git clone [https://github.com/yourusername/image-cryptography.git](https://github.com/Amey-Chougule/Image-Cryptography.git)
cd image-cryptography

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the tool
python main.py

