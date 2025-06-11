from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20)
    developer = models.CharField(max_length=20)
    bio = models.TextField(max_length=255)
    release_year = models.DateTimeField(null = True)
    is_rented = models.BooleanField(default = False)
    amount = models.DecimalField(decimal_places=10, max_digits=20)
    created_by = models.ForeignKey(User, related_name= 'user', on_delete=models.CASCADE, null=True)

