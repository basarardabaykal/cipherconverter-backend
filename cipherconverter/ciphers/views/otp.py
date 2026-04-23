import os

import grpc
from rest_framework.exceptions import APIException, ValidationError

from .base import BaseViewSet
from ..models import OTP
from ..serializers import OTPSerializer
from ..grpc import symmetric_pb2, symmetric_pb2_grpc


class OTPViewSet(BaseViewSet):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

    def process_cipher(self, data):
        address = os.getenv("MICROSERVICE_URL")
        if not address:
            raise APIException(detail="MICROSERVICE_URL is not configured")

        request = symmetric_pb2.OTPRequest(
            text=data["input_text"].encode("utf-8"),
            key=data["key"].encode("utf-8"),
        )

        try:
            with grpc.insecure_channel(address) as channel:
                stub = symmetric_pb2_grpc.CipherServiceStub(channel)
                if data["operation"] == OTP.Operation.ENCRYPT:
                    response = stub.EncryptOTP(request, timeout=3)
                elif data["operation"] == OTP.Operation.DECRYPT:
                    response = stub.DecryptOTP(request, timeout=3)
                else:
                    raise ValidationError({"operation": "Invalid operation."})
        except grpc.RpcError as exc:
            exc_503 = APIException(
                detail=f"Cipher microservice unavailable ({exc.code().name})"
            )
            exc_503.status_code = 503
            raise exc_503 from exc

        return response.result.decode("utf-8")