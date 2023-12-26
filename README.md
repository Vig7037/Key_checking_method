
# Encryption/Decryption Script with Key_checking_method

This Python script provides a basic encryption and decryption mechanism using XOR operations. It takes user input, encrypts the data, and then allows decryption with a key.

## Encryption

To encrypt data, the script takes user input and XORs each byte with a randomly generated key. The encrypted data is then stored in a file, along with a file number used for verification.

## Decryption

Decryption requires a key and the correct file number. The script reads the encrypted data and key from files, verifies the file number, and performs XOR decryption to reveal the original data.

## Usage

1. Run the encryption script:
    ```bash
    python encryption_script.py
    ```

2. Enter the data when prompted, and the script will generate encrypted data in a file.

3. Run the decryption script:
    ```bash
    python decryption_script.py
    ```

4. Enter the key when prompted, and the script will decrypt the data if the key is valid.

## Files

- `encryption_script.py`: Encrypts user input and stores the result in a file.
- `decryption_script.py`: Decrypts data from the file using a key and file number.

## Example

```bash
$ python encryption_script.py
Enter the data: Hello, World!
Your data is encrypted. Now your data is safe.

$ python decryption_script.py
Enter the key: 1234
Hello, World!
```
