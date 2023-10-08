from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

# Create your models here.
