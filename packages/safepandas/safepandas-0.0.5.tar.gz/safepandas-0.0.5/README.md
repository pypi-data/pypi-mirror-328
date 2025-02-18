# SafePandas  
**Privacy-Preserving DataFrames with Homomorphic Encryption**  

SafePandas is a lightweight wrapper around Pandas that enables computations on encrypted data using Homomorphic Encryption. With SafePandas, your sensitive data remains encrypted throughout processing, ensuring privacy and security. Only when explicitly requested does decryption occur, allowing for controlled and secure data analysis.  

## Features  

- **Automatic Encryption** – DataFrame values are encrypted upon creation.  
- **Compute on Encrypted Data** – Perform mathematical operations without decryption.  
- **Controlled Decryption** – Decrypt only when explicitly required.  
- **Seamless Pandas Compatibility** – Works like Pandas with minimal changes.  
- **Secure Data Storage** – Save encrypted DataFrames and load them securely.  
- **Homomorphic Encryption** – Uses Pyfhel for secure computations.  

## Installation  

SafePandas requires Python 3.7 or later. Install it using:  

```bash
pip install safepandas

