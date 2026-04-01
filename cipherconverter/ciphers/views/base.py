from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from rest_framework import status
from core import DetailedResponse

class BaseViewSet(GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def process_cipher(self, data):
        # Implement this in viewsets inheriting BaseViewSet
        raise NotImplementedError

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        output_text = self.process_cipher(serializer.validated_data)

        instance = serializer.save(
            output_text=output_text,
        )

        return DetailedResponse(
            status=status.HTTP_200_OK,
            status_message="Success",
            message="Successfully processed cipher.",
            content=self.get_serializer(instance).data,
        )

