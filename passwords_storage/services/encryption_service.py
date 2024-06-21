from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self, key: bytes):
        self.cipher_suite = Fernet(key)

    def encrypt(self, plain_text: str) -> str:
        encrypted_text = self.cipher_suite.encrypt(plain_text.encode())
        return encrypted_text.decode()

    def decrypt(self, encrypted_text: str) -> str:
        plain_text = self.cipher_suite.decrypt(encrypted_text.encode())
        return plain_text.decode()
