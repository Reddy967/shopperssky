from django.db import models

# Create your models here.

class Register(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
