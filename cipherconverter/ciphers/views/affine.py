from views import BaseViewSet
from models import Affine
from serializers import AffineSerializer

class AffineViewSet(BaseViewSet):
    queryset=Affine.objects.all()
    serializer_class=AffineSerializer

    def process_cipher(self, data):
        #call microservice
        pass