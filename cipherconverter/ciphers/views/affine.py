import os

import grpc
from rest_framework.exceptions import APIException, ValidationError

from .base import BaseViewSet
from ..models import Affine
from ..serializers import AffineSerializer
from ..grpc import symmetric_pb2, symmetric_pb2_grpc

class AffineViewSet(BaseViewSet):
    queryset=Affine.objects.all()
    serializer_class=AffineSerializer

    def process_cipher(self, data):
        address = os.getenv("MICROSERVICE_URL")

        if not address:
            raise APIException(detail="MICROSERVICE_URL is not configured")

        request = symmetric_pb2.AffineRequest(
            text=data["input_text"].encode("utf-8"),
            a=data["a"],
            b=data["b"],
        )

        try:
            with grpc.insecure_channel(address) as channel:
                stub = symmetric_pb2_grpc.CipherServiceStub(channel)
                if data["operation"] == Affine.Operation.ENCRYPT:
                    response = stub.EncryptAffine(request, timeout=3)
                elif data["operation"] == Affine.Operation.DECRYPT:
                    response = stub.DecryptAffine(request, timeout=3)
                else:
                    raise ValidationError({"operation": "Invalid operation."})
        except grpc.RpcError as exc:
            exc_503 = APIException(
                detail=f"Cipher microservice unavailable ({exc.code().name})"
            )
            exc_503.status_code = 503
            raise exc_503 from exc

        return response.result.decode("utf-8")