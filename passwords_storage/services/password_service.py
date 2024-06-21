from ..models import PasswordEntry
from .encryption_service import EncryptionService

class PasswordService:
    def __init__(self, encryption_service: EncryptionService):
        self.encryption_service = encryption_service

    def create_or_update_password(self, service_name: str, password: str) -> PasswordEntry:
        encrypted_password = self.encryption_service.encrypt(password)
        entry, created = PasswordEntry.objects.update_or_create(
            service_name=service_name,
            defaults={'encrypted_password': encrypted_password}
        )
        return entry

    def get_password(self, service_name: str) -> str:
        entry = PasswordEntry.objects.get(service_name=service_name)
        return self.encryption_service.decrypt(entry.encrypted_password)

    def search_passwords(self, partial_service_name: str):
        entries = PasswordEntry.objects.filter(service_name__icontains=partial_service_name)
        return [
            {
                'service_name': entry.service_name,
                'password': self.encryption_service.decrypt(entry.encrypted_password)
            } for entry in entries
        ]
