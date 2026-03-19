from views import BaseViewSet
from models import Caesar
from serializers import CaesarSerializer

class CaesarViewSet(BaseViewSet):
    queryset = Caesar.objects.all()
    serializer_class = CaesarSerializer

    def process_cipher(self, data):
        #call microservice function here
        pass
