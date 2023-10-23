from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50) # ok
    email = models.CharField(max_length=75) # ok
    notes = models.TextField() # ok

    def __str__(self):
        return self.name