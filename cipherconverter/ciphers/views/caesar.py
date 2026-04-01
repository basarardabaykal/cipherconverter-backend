import os

import grpc
from rest_framework.exceptions import APIException, ValidationError

from .base import BaseViewSet
from ..models import Caesar
from ..serializers import CaesarSerializer
from ..grpc import cipher_pb2, cipher_pb2_grpc

class CaesarViewSet(BaseViewSet):
    queryset = Caesar.objects.all()
    serializer_class = CaesarSerializer

    def process_cipher(self, data):
        address = os.getenv("CIPHER_MICROSERVICE_ADDR", "microservice:50051")
        request = cipher_pb2.CaesarRequest(
            text=data["input_text"].encode("utf-8"),
            shift=data["key"],
        )

        try:
            with grpc.insecure_channel(address) as channel:
                stub = cipher_pb2_grpc.CipherServiceStub(channel)
                if data["operation"] == Caesar.Operation.ENCRYPT:
                    response = stub.EncryptCaesar(request, timeout=3)
                elif data["operation"] == Caesar.Operation.DECRYPT:
                    response = stub.DecryptCaesar(request, timeout=3)
                else:
                    raise ValidationError({"operation": "Invalid operation."})
        except grpc.RpcError as exc:
            exc_503 = APIException(
                detail=f"Cipher microservice unavailable ({exc.code().name})"
            )
            exc_503.status_code = 503
            raise exc_503 from exc

        return response.result.decode("utf-8")
