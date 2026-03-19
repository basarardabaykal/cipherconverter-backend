from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from models import BaseCipher

class Caesar(BaseCipher):
    key = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(26)])