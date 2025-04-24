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
    print("\nBrute-force Caesar Decryption Results:")
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift}: {decrypted}")

def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

def xor_brute_force(text):
    print("\nBrute-force XOR Decryption Results:")
    for key in range(1, 256):
        try:
            decrypted = xor_encrypt_decrypt(text, key)
            print(f"Key {key}: {decrypted}")
        except Exception:
            continue

def main():
    print("Encryption Tool (Caesar & XOR)")
    print("Use responsibly and for educational purposes only.")
    
    print("\nAvailable Modes:")
    print(" 1. Caesar Encrypt (C-E)")
    print(" 2. Caesar Decrypt (C-D)")
    print(" 3. Caesar Brute-force (C-B)")
    print(" 4. XOR Encrypt/Decrypt (X-E)")
    print(" 5. XOR Brute-force (X-B)")

    choice = input("\nSelect a mode: ").strip().upper()

    if choice not in ['C-E', 'C-D', 'C-B', 'X-E', 'X-B']:
        print("Invalid choice!")
        return

    text = input("Enter the message: ").strip()

    if choice == 'C-B':
        caesar_brute_force(text)

    elif choice in ['C-E', 'C-D']:
        while True:
            shift_input = input("Enter Caesar shift value (integer): ").strip()
            try:
                shift = int(shift_input)
                break
            except ValueError:
                print("Invalid shift! Enter a valid integer.")
        
        if choice == 'C-E':
            result = caesar_encrypt(text, shift)
            print("Encrypted (Caesar):", result)
        else:
            result = caesar_decrypt(text, shift)
            print("Decrypted (Caesar):", result)

    elif choice == 'X-E':
        while True:
            key_input = input("Enter XOR key (0–255): ").strip()
            try:
                key = int(key_input)
                if 0 <= key <= 255:
                    break
                else:
                    print("Key must be between 0 and 255.")
            except ValueError:
                print("Invalid key! Enter an integer between 0 and 255.")
        
        result = xor_encrypt_decrypt(text, key)
        print("XOR Result:", result)

    elif choice == 'X-B':
        xor_brute_force(text)

if __name__ == "__main__":
    main()
