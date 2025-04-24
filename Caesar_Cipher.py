import string
import binascii

# ------------------ Caesar Cipher ------------------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_brute_force(text):
    print("\n🔍 Caesar Cipher Brute-force Decryption:\n")
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2}: {decrypted}")
    print("-" * 50)

# ------------------ XOR Cipher ------------------
def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

def xor_encrypt_to_hex(text, key):
    encrypted = bytes([ord(c) ^ key for c in text])
    return encrypted.hex()

def xor_decrypt_from_hex(hex_cipher, key):
    ciphertext = bytes.fromhex(hex_cipher)
    return ''.join(chr(b ^ key) for b in ciphertext)

def xor_brute_force(hex_cipher):
    print("\n🔍 XOR Brute-force (Hex Input) Decryption:\n")
    ciphertext = bytes.fromhex(hex_cipher)
    for key in range(256):
        try:
            decoded = ''.join(chr(b ^ key) for b in ciphertext)
            if all(32 <= ord(c) <= 126 or c in "\n\r\t" for c in decoded):  # printable
                ascii_key = chr(key) if 32 <= key <= 126 else "Non-printable"
                print(f"Key (int): {key:3}, Key (ASCII): {ascii_key}\nDecrypted Message: {decoded}\n{'-'*50}")
        except Exception:
            continue

# ------------------ Combined CLI ------------------
def main():
    print("🔐 Combined Encryption Tool: Caesar Cipher + XOR Cipher\n")
    print("📌 Choose an Option:")
    print(" 1. Caesar Encrypt")
    print(" 2. Caesar Decrypt")
    print(" 3. Caesar Brute-force")
    print(" 4. XOR Encrypt (to Hex)")
    print(" 5. XOR Decrypt (from Hex)")
    print(" 6. XOR Brute-force (from Hex)")

    choice = input("\nEnter your choice (1–6): ").strip()

    if choice in ['1', '2', '3']:
        text = input("Enter the message: ").strip()
        if choice == '3':
            caesar_brute_force(text)
        else:
            while True:
                try:
                    shift = int(input("Enter Caesar shift value (integer): ").strip())
                    break
                except ValueError:
                    print("❗ Invalid input. Enter a valid integer.")
            if choice == '1':
                result = caesar_encrypt(text, shift)
                print("✅ Caesar Encrypted:", result)
            else:
                result = caesar_decrypt(text, shift)
                print("✅ Caesar Decrypted:", result)

    elif choice in ['4', '5', '6']:
        if choice == '6':
            hex_cipher = input("Enter hex-encoded XOR cipher text: ").strip()
            xor_brute_force(hex_cipher)
        else:
            if choice == '4':
                text = input("Enter plaintext to encrypt: ").strip()
            else:
                hex_cipher = input("Enter hex-encoded cipher: ").strip()

            while True:
                try:
                    key = int(input("Enter XOR key (0–255): ").strip())
                    if 0 <= key <= 255:
                        break
                    else:
                        print("❗ Key must be between 0 and 255.")
                except ValueError:
                    print("❗ Invalid input. Enter a number between 0 and 255.")

            if choice == '4':
                hex_output = xor_encrypt_to_hex(text, key)
                print("✅ XOR Encrypted (Hex):", hex_output)
            else:
                result = xor_decrypt_from_hex(hex_cipher, key)
                print("✅ XOR Decrypted:", result)
    else:
        print("❌ Invalid option. Try again!")

if __name__ == "__main__":
    main()
