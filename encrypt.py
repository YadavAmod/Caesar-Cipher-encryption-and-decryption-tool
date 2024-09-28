import argparse

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encryption/Decryption Tool")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("text", help="Text to encrypt or decrypt")
    parser.add_argument("shift", type=int, help="Shift value for the cipher")
    
    args = parser.parse_args()
    
    if args.action == "encrypt":
        result = encrypt(args.text, args.shift)
        print(f"Encrypted text: {result}")
    else:
        result = decrypt(args.text, args.shift)
        print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()