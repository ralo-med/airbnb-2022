from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class House(models.Model):

    """Model Definition for House"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(help_text="Positive Numbers only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_friendly = models.BooleanField(
        default=False, help_text="Does this house allow pets?"
    )

    def __str__(self):
        return self.name
