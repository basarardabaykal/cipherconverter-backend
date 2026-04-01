from django.urls import path
from .views import CaesarViewSet, AffineViewSet

urlpatterns = [
    path("caesar/", CaesarViewSet.as_view({"post": "create"}), name="ciphers-caesar"),
    path("affine/", AffineViewSet.as_view({"post": "create"}), name="ciphers-affine"),
]
