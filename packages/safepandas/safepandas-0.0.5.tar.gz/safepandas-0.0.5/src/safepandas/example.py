import safepandas as pd

# Create a DataFrame
data = {'age': [25, 30, 35, 40]}
key_path = "my_encryption_key"  # Path to save/load the key

df = pd.SafePandas(data, key=key_path)  # Pass the key path during DataFrame creation

# Perform operations (data stays encrypted)
df['age'] = df['age'].apply(lambda x: df.encryption.encrypt(df.encryption.decrypt(x) + 5))

# Save the encrypted DataFrame to a CSV file
df.to_csv("encrypted_data.csv", format="csv")

# Load the encrypted DataFrame from the CSV file, providing the key
loaded_df = pd.SafePandas.read_csv("encrypted_data.csv", format="csv", key=key_path)

# Decrypt the data
decrypted_df = loaded_df.decrypt()

# Display the decrypted result
print("Decrypted Data:")
print(decrypted_df)
