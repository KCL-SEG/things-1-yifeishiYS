from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField()
    quantity = models.IntegerField()

# Create your models here.
