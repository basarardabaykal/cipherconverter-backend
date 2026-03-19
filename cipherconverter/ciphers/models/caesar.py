from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from models import CipherBase

class Caesar(CipherBase):
    key = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(26)])