def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force_decrypt(text):
    print("\nBrute-force Decryption Results:")
    for shift in range(26):
        decrypted = decrypt(text, shift)
        print(f"Shift {shift}: {decrypted}")

def main():
    print("Caesar Cipher Program")
    print("Ensure you use this tool responsibly and only for educational purposes.")
    
    choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (B)rute-force decrypt? ").strip().upper()

    if choice not in ['E', 'D', 'B']:
        print("Invalid choice!")
        return

    text = input("Enter the message: ").strip()
    
    if choice == 'B':
        brute_force_decrypt(text)
    else:
        while True:
            shift_input = input("Enter the shift value: ").strip()
            try:
                shift = int(shift_input)
                break
            except ValueError:
                print("Invalid shift value! Please enter a valid integer.")

        if choice == 'E':
            result = encrypt(text, shift)
            print("Encrypted message:", result)
        elif choice == 'D':
            result = decrypt(text, shift)
            print("Decrypted message:", result)

if __name__ == "__main__":
    main()
