from django.db import models


class PasswordEntry(models.Model):
    service_name = models.CharField(max_length=255, unique=True)
    encrypted_password = models.CharField(max_length=255)

    def __str__(self):
        return self.service_name
