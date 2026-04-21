from django.contrib import admin
from django.urls import include, path

from .views import healthcheck

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/healthcheck/", healthcheck, name="healthcheck"),
    path("api/auth/", include("users.urls")),
    path("api/ciphers/", include("ciphers.urls")),
]
