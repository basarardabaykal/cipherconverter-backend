from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from rest_framework import status
from core import DetailedResponse

class BaseViewSet(GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def process_cipher(self):
        # Implement this in viewsets inheriting BaseViewSet
        pass

    def create(self, request, *args, **kwargs):
        #parse input
        result = self.process_cipher()
        return DetailedResponse(status=status.HTTP_200_OK, status_message="Success", message="Successfully processed cipher.", content=result)

