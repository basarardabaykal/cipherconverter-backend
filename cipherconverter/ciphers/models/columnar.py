from django.db import models
from .base import BaseCipher

class Columnar(BaseCipher):
    key = models.IntegerField()