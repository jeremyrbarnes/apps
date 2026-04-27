"""
models module
"""
from django.db import models


# Create your models here.
class Player(models.Model):
    """
    Player class
    """
    email_address = models.EmailField(null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    height = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=True)

    def __str__(self):
        """ returns a string representation of this model """
        return f"'{self.last_name}, {self.first_name}; {self.email_address}"
