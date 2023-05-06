from django.db import models


class People(models.Model):
    name = models.CharField(max_length=10, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
