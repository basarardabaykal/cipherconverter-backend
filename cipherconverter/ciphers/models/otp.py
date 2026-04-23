from django.db import models

from .base import BaseCipher


class OTP(BaseCipher):
    key = models.TextField()
