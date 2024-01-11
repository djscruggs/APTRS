from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=300,unique = True)
    img = models.ImageField(upload_to='company')
    address = models.TextField()