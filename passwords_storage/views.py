from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PasswordEntrySerializer
from .services.password_service import PasswordService
from .services.encryption_service import EncryptionService
from django.conf import settings


class PasswordView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        encryption_service = EncryptionService(settings.ENCRYPTION_KEY)
        self.password_service = PasswordService(encryption_service)

    def post(self, request, service_name):
        serializer = PasswordEntrySerializer(data=request.data)
        if serializer.is_valid():
            self.password_service.create_or_update_password(
                service_name, serializer.validated_data['password']
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, service_name=None):
        if service_name:
            password = self.password_service.get_password(service_name)
            return Response({
                'service_name': service_name,
                'password': password
            }, status=status.HTTP_200_OK)
        partial_service_name = request.query_params.get('service_name')
        if partial_service_name:
            entries = self.password_service.search_passwords(partial_service_name)
            return Response(entries, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
