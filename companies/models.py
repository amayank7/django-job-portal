from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    name_lower = models.CharField(max_length = 64, unique = True)
    logo = models.ImageField(upload_to = 'logos', null = True, blank = True)
    about = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.name

