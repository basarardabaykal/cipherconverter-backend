from django.db import models
from django.conf import settings

class CipherBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_%(class)s",
    )
    input_text = models.TextField()
    output_text = models.TextField()

    class Operation(models.TextChoices):
        ENCRYPT = "encrypt", "Encrypt"
        DECRYPT = "decrypt", "Decrypt"

    operation = models.CharField(
        max_length=10, choices=Operation.choices, db_index=True
    )

    class Meta:
        abstract = True
