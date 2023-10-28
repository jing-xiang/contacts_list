from django.db import models

# Create your models here.
from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name