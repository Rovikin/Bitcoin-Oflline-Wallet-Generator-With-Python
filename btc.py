import os
import base58
import ecdsa
from Crypto.Hash import SHA256, RIPEMD160
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import getpass

def generate_bitcoin_address(password):
    # Generate private key
    private_key = os.urandom(32)

    # Get compressed public key
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    x = vk.pubkey.point.x()
    y = vk.pubkey.point.y()
    compressed_public_key = '02' if y % 2 == 0 else '03'
    compressed_public_key += x.to_bytes(32, 'big').hex()

    # Generate WIF for compressed private key
    fullkey = '80' + private_key.hex() + '01'
    sha256a = SHA256.new(bytes.fromhex(fullkey)).hexdigest()
    sha256b = SHA256.new(bytes.fromhex(sha256a)).hexdigest()
    WIF = base58.b58encode(bytes.fromhex(fullkey + sha256b[:8])).decode()

    # Encrypt WIF with password using AES-256
    key = SHA256.new(password.encode()).digest()  # Full 32-byte key
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_wif = iv + cipher.encrypt(pad(WIF.encode(), AES.block_size))

    # Get P2PKH address (Legacy Address)
    hash160 = RIPEMD160.new()
    hash160.update(SHA256.new(bytes.fromhex(compressed_public_key)).digest())
    public_key_hash = '00' + hash160.hexdigest()
    checksum = SHA256.new(SHA256.new(bytes.fromhex(public_key_hash)).digest()).hexdigest()[:8]
    p2pkh_address = base58.b58encode(bytes.fromhex(public_key_hash + checksum)).decode()

    return {
        'encrypted_wif': encrypted_wif.hex(),
        'p2pkh_address': p2pkh_address,
    }

def decrypt_wif(encrypted_wif_hex, password):
    encrypted_wif = bytes.fromhex(encrypted_wif_hex)
    iv = encrypted_wif[:16]
    ciphertext = encrypted_wif[16:]

    key = SHA256.new(password.encode()).digest()  # Full 32-byte key
    cipher = AES.new(key, AES.MODE_CBC, iv)
    wif = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

    # Recalculate the P2PKH (Legacy) address from the decrypted WIF
    private_key = base58.b58decode(wif)[1:-5]
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    x = vk.pubkey.point.x()
    y = vk.pubkey.point.y()
    compressed_public_key = '02' if y % 2 == 0 else '03'
    compressed_public_key += x.to_bytes(32, 'big').hex()

    hash160 = RIPEMD160.new()
    hash160.update(SHA256.new(bytes.fromhex(compressed_public_key)).digest())
    public_key_hash = '00' + hash160.hexdigest()
    checksum = SHA256.new(SHA256.new(bytes.fromhex(public_key_hash)).digest()).hexdigest()[:8]
    p2pkh_address = base58.b58encode(bytes.fromhex(public_key_hash + checksum)).decode()

    return wif, p2pkh_address

def main():
    print("1. Create wallet")
    print("2. Decrypt private key")
    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            password = getpass.getpass("Create your password: ")
            confirm_password = getpass.getpass("Confirm your password: ")
            if password == confirm_password:
                break
            else:
                print("Passwords do not match. Please try again.")

        address_info = generate_bitcoin_address(password)
        
        # Save the encrypted WIF and legacy address to files
        with open("encrypted_key.txt", "w") as f:
            f.write(address_info['encrypted_wif'])
        with open("legacy_address.txt", "w") as f:
            f.write(address_info['p2pkh_address'])

        print("\n========= Wallet created successfully! ===========")
        print("\nKeys have been saved to : \n\n==>> encrypted_key.txt \n\nand : \n\n==>> legacy_address.txt\n\n=================================================")

    elif choice == '2':
        encrypted_wif_hex = input("Enter your encrypted private key: ")
        password = getpass.getpass("Enter your password: ")
        try:
            decrypted_wif, p2pkh_address = decrypt_wif(encrypted_wif_hex, password)
            print(f"\nDecrypted key: \n{decrypted_wif}\n")
            print(f"Legacy Address : \n{p2pkh_address}\n")
        except ValueError:
            print("Incorrect password or corrupted key!")

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()