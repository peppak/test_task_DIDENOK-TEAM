from rest_framework import serializers
from .models import PasswordEntry


class PasswordEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordEntry
        fields = ['password']

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return PasswordEntry(**validated_data)
