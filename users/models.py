from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import EmailField, ImageField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    display_picture = models.ImageField(null = True, blank = True)
    about = models.TextField(null = True, blank = True)
    age = models.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(110)], null = True, blank = True)
    experience_in_years = models.IntegerField(validators=[MaxValueValidator(60)], null = True, blank = True)
    phone = models.CharField(max_length=10, validators=[RegexValidator('[0-9]{10}')], null = True, blank = True)