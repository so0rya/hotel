from django.db import models

# Create your models here.

class Dishes(models.Model):
    name=models.CharField(max_length=120)
    category=models.CharField(max_length=150)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name
