import os

import grpc
from rest_framework.exceptions import APIException, ValidationError

from .base import BaseViewSet
from ..models import Columnar
from ..serializers import ColumnarSerializer
from ..grpc import cipher_pb2, cipher_pb2_grpc


class ColumnarViewSet(BaseViewSet):
    queryset = Columnar.objects.all()
    serializer_class = ColumnarSerializer

    def process_cipher(self, data):
        address = os.getenv("MICROSERVICE_URL")
        if not address:
            raise APIException(detail="MICROSERVICE_URL is not configured")

        request = cipher_pb2.ColumnarRequest(
            text=data["input_text"].encode("utf-8"),
            columns=data["key"],
        )

        try:
            with grpc.insecure_channel(address) as channel:
                stub = cipher_pb2_grpc.CipherServiceStub(channel)
                if data["operation"] == Columnar.Operation.ENCRYPT:
                    response = stub.EncryptColumnar(request, timeout=3)
                elif data["operation"] == Columnar.Operation.DECRYPT:
                    response = stub.DecryptColumnar(request, timeout=3)
                else:
                    raise ValidationError({"operation": "Invalid operation."})
        except grpc.RpcError as exc:
            exc_503 = APIException(
                detail=f"Cipher microservice unavailable ({exc.code().name})"
            )
            exc_503.status_code = 503
            raise exc_503 from exc

        return response.result.decode("utf-8")