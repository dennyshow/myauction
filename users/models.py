from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    firstname = models.CharField(max_length=45, default='')
    lastname = models.CharField(max_length=60)
    email = models.EmailField()
    username = models.CharField(max_length=45)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    def __str__(self):
        return "(" + self.firstname + ", " + self.lastname + ", " + self.email + ", " + self.username + ", " + self.balance + ")"