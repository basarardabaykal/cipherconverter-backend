from django.db import models
from django.conf import settings

class Operation(models.TextChoices):
    ENCRYPT = "encrypt", "Encrypt"
    DECRYPT = "decrypt", "Decrypt"

class CipherBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_%(class)s",
    )
    input_text = models.TextField()
    output_text = models.TextField()
    operation = models.CharField(max_length=10, choices=Operation.choices)

    class Meta:
        abstract = True
