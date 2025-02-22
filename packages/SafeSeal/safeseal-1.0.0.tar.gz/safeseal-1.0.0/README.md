# SafeSeal

**SafeSeal** is a Python encryption library that securely encrypts and decrypts data using multiple layers of encoding and compression.

## 🚀 Features
- Multi-layered encryption: `pickle` → `marshal` → `base64` → `zlib` → `gzip`
- Multi-layered decryption: `gzip` → `zlib` → `base64` → `marshal` → `pickle`
- Simple and Pythonic API
- Handles errors gracefully

## 🔧 Installation

Install SafeSeal using pip:

```bash
pip install SafeSeal
```

Or clone the repository:

```bash
git clone https://github.com/Altikrity/SafeSeal.git
cd SafeSeal
python setup.py install
```

## 📦 Usage

### Import SafeSeal

```python
from SafeSeal import Cencrypt, Cdecrypt
```

### Encrypt Data

```python
data = "Hello, SafeSeal!"
encrypted_data = Cencrypt(data)
print(f"Encrypted: {encrypted_data}")
```

### Decrypt Data

```python
decrypted_data = Cdecrypt(encrypted_data)
print(f"Decrypted: {decrypted_data}")
```

## 🔍 Example

```python
from SafeSeal import Cencrypt, Cdecrypt

# Original data
data = "This is a secret message."

# Encrypt the data
encrypted = Cencrypt(data)
print("Encrypted Data:", encrypted)

# Decrypt the data
decrypted = Cdecrypt(encrypted)
print("Decrypted Data:", decrypted)
```

## ⚠️ Notes
- This library is designed for obfuscation and lightweight encryption.
- `marshal` is Python-version-dependent, so encrypted data may not be compatible across different Python versions.
- Not recommended for high-security applications — for that, consider using `cryptography` or `pycryptodome`.

## 🛠️ Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 📜 License
This project is licensed under the MIT License.

---

✨ Built with ❤️ by [Your Name].

---

Ready to keep your secrets safe? Seal them with **SafeSeal**! 🔐

