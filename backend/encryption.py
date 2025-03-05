
from cryptography.fernet import Fernet

# Generate a key (should be securely stored in a config file)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    # Encrypts data before storing or transmitting
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt_data(encrypted_data):
    # Decrypts data when retrieving from storage
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

# Example usage
if __name__ == "__main__":
    sample_text = "Sensitive Patient Data"
    encrypted_text = encrypt_data(sample_text)
    decrypted_text = decrypt_data(encrypted_text)
    
    print(f"Original: {sample_text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
