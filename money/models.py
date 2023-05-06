from django.db import models

# Create your models here

class People(models.Model):
    name = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
