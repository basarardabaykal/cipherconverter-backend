from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from rest_framework import status
from core import DetailedResponse

class BaseViewSet(GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def process_cipher(self, data):
        # Implement this in viewsets inheriting BaseViewSet
        pass

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = self.process_cipher(serializer.validated_data)

        instance = serializer.save(
            output_text=result.output_text  # placeholder
            # other fields
        )

        return DetailedResponse(
            status=status.HTTP_200_OK,
            status_message="Success",
            message="Successfully processed cipher.",
            content=instance,
        )

