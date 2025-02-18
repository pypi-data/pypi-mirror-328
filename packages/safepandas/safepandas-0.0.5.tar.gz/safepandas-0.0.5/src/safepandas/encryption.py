import os
from pyseal import PySEAL

class HomomorphicEncryption:
    def __init__(self, key=None):
        """
        Initialize the encryption system with a provided key.
        If no key is provided, generate a new key.
        """
        self.he = PySEAL()
        
        if key:
            self.load_key(key)
        else:
            self.he.keyGen()
    
    def encrypt(self, data):
        """Encrypt the data using Homomorphic Encryption."""
        return self.he.encrypt(data)

    def decrypt(self, encrypted_data):
        """Decrypt the data using the private key."""
        return self.he.decrypt(encrypted_data)

    def save_key(self, file_path):
        """Save the encryption key (public and private) to a file."""
        self.he.save_public_key(file_path + "_public.key")
        self.he.save_private_key(file_path + "_private.key")

    def load_key(self, file_path):
        """Load the encryption key from files."""
        if not os.path.exists(file_path + "_public.key") or not os.path.exists(file_path + "_private.key"):
            raise ValueError(f"Key files not found at {file_path}")
        self.he.load_public_key(file_path + "_public.key")
        self.he.load_private_key(file_path + "_private.key")
