# Caesar-Cipher-encryption-and-decryption-tool
. The Caesar Cipher is a type of substitution cipher where each letter in the text is shifted by a fixed number of positions in the alphabet.

Here’s a detailed explanation of the code and how to run it:

Tools Required:
Python: Make sure you have Python installed on your system. You can download and install it from python.org.
Command Line (Terminal): You will run this script from the command line.

Code Explanation:

Imports:
import argparse
The argparse module is used for parsing command-line arguments, allowing the user to specify actions and inputs directly from the terminal.

encrypt(text, shift): This function performs encryption using the Caesar Cipher. It takes two arguments:

text: The text to be encrypted.
shift: The number of positions by which each character in the text will be shifted.
Logic:

For each character in the text:
Check if the character is an alphabet letter (char.isalpha()).
If it is a letter, determine if it’s uppercase or lowercase using ascii_offset (65 for uppercase A, 97 for lowercase a).
Compute the new character by shifting it within the alphabet using the formula:
shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
The modulo operation (% 26) ensures the shift wraps around if it exceeds the length of the alphabet.
Non-alphabet characters remain unchanged.
Example: Encrypting "HELLO" with a shift of 3 would produce "KHOOR".

decrypt(text, shift): This function decrypts the text by simply calling the encrypt function with a negative shift (-shift), effectively reversing the cipher.

main(): This is the entry point of the program where command-line arguments are parsed and actions are performed.

argparse.ArgumentParser is used to define the required arguments:
action: Whether to "encrypt" or "decrypt" the text.
text: The text to be processed.
shift: The integer shift value for the cipher.
Based on the user’s input, the program either encrypts or decrypts the text and prints the result.

Running the Program: The if __name__ == "__main__": block ensures that the main() function runs when the script is executed.

How to Run the Code:
Save the script to a file, e.g., caesar_cipher.py.

Open the terminal and navigate to the directory where the script is saved.

Run the script using the following commands:

For encryption:
python caesar_cipher.py encrypt "HELLO" 3
This will output: Encrypted text: KHOOR

For decryption:
python caesar_cipher.py decrypt "KHOOR" 3
This will output: Decrypted text: HELLO
Breakdown of Command Arguments:
"encrypt": Specifies the action to perform (can be either "encrypt" or "decrypt").
"HELLO": The text to encrypt or decrypt.
3: The shift value for the Caesar Cipher.

Required Setup:
Ensure Python is installed (version 3.x recommended).
You can check the installation by running:
python --version

Run the script with the correct arguments as described.

This is a simple example of using Python to build a command-line tool for Caesar Cipher encryption and decryption.









