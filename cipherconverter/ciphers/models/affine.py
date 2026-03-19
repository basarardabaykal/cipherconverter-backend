from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from models import BaseCipher

class Affine(BaseCipher):
    class A(models.IntegerChoices):
        A1 = 1, "1"
        A3 = 3, "3"
        A5 = 5, "5"
        A7 = 7, "7"
        A9 = 9, "9"
        A11 = 11, "11"
        A15 = 15, "15"
        A17 = 17, "17"
        A19 = 19, "19"
        A21 = 21, "21"
        A23 = 23, "23"
        A25 = 25, "25"
            
    a = models.IntegerField(choices=A.choices)
    b = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])