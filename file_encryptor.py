import os
import getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

def encrypt_file(file_name, password):
    # Generate 256-bit key from password
    key = SHA256.new(password.encode()).digest()
    
    # Create AES cipher
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    
    # Read file data
    with open(file_name, 'rb') as f:
        file_data = f.read()
    
    # Encrypt data
    encrypted_data = iv + cipher.encrypt(pad(file_data, AES.block_size))
    
    # Write encrypted data back to file
    with open(file_name + ".enc", 'wb') as f:
        f.write(encrypted_data)
    
    print(f"File '{file_name}' has been encrypted and saved as '{file_name}.enc'")

def decrypt_file(file_name, password):
    # Generate 256-bit key from password
    key = SHA256.new(password.encode()).digest()
    
    # Read encrypted file data
    with open(file_name, 'rb') as f:
        encrypted_data = f.read()
    
    # Extract IV and encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]
    
    # Create AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt data
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    except ValueError:
        print("Incorrect password or corrupted file!")
        return
    
    # Write decrypted data back to file
    with open(file_name[:-4], 'wb') as f:  # Remove '.enc' from file name
        f.write(decrypted_data)
    
    print(f"File '{file_name}' has been decrypted and saved as '{file_name[:-4]}'")

def main():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter your choice: ")

    if choice == '1':
        file_name = input("Enter the file name to encrypt: ")
        password = getpass.getpass("Enter the password: ")
        encrypt_file(file_name, password)
    
    elif choice == '2':
        file_name = input("Enter the encrypted file name to decrypt: ")
        password = getpass.getpass("Enter the password: ")
        decrypt_file(file_name, password)
    
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()