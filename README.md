#Caesar Cipher Implementation in Python
This repository contains a simple and educational implementation of the Caesar Cipher in Python.
The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places in the alphabet. It is one of the earliest and simplest forms of encryption.

🚀 Features
🔐 Encryption: Encrypts plaintext by shifting each letter by a specified number of positions.

#🔓 Decryption: Reverses the encryption by shifting letters back using the same shift value.

🧠 Brute-force Decryption: Tries all 26 possible shift values to guess the original message (helpful if the shift is unknown).

🔤 Case Preservation: Maintains the original case (uppercase or lowercase) of letters.

🔣 Non-Alphabetic Characters: Keeps symbols, numbers, and spaces unchanged during encryption/decryption.

🛠️ How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/raghavmishra1/Implement-Caesar-Cipher
cd Implement-Caesar-Cipher
Run the script:

bash
Copy
Edit
python caesar_cipher.py
Choose an option:

(E) Encrypt a message

(D) Decrypt a message

(B) Brute-force decrypt without knowing the shift

📂 File Structure
caesar_cipher.py: Main script with encryption, decryption, and brute-force logic.

LICENSE: Project license (MIT).

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

