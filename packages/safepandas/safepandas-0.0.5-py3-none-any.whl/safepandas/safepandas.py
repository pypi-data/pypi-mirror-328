import pandas as pd
from .encryption import HomomorphicEncryption

class SafePandas(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super().__init__(*args, **kwargs)
        
        if key:
            self.encryption = HomomorphicEncryption(key)
        else:
            self.encryption = HomomorphicEncryption()
        
        self.encrypted = True
        self._encrypt_data()

    def _encrypt_data(self):
        for column in self.columns:
            self[column] = self[column].apply(lambda x: self.encryption.encrypt(x))

    def decrypt(self):
        decrypted_data = {column: self[column].apply(lambda x: self.encryption.decrypt(x)) for column in self.columns}
        decrypted_df = pd.DataFrame(decrypted_data)
        decrypted_df.encrypted = False
        return decrypted_df

    def to_csv(self, file_path, format="csv"):
        if format == "csv":
            super().to_csv(file_path, index=False)
        elif format == "pickle":
            super().to_pickle(file_path)
        else:
            raise ValueError("Unsupported format. Use 'csv' or 'pickle'.")
        
        self.encryption.save_key("encryption_key")

    @classmethod
    def read_csv(cls, file_path, format="csv", key=None):
        if format == "csv":
            encrypted_df = pd.read_csv(file_path)
        elif format == "pickle":
            encrypted_df = pd.read_pickle(file_path)
        else:
            raise ValueError("Unsupported format. Use 'csv' or 'pickle'.")
        
        if not key:
            raise ValueError("A decryption key is required for loading encrypted data.")
        
        return cls(encrypted_df, key=key)
