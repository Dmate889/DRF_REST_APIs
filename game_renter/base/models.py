from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20, unique=True)
    developer = models.CharField(max_length=50)
    bio = models.TextField(max_length=255)
    release_year = models.DateTimeField(null = True)
    is_rented = models.BooleanField(default = False)
    price = models.DecimalField(decimal_places=2, max_digits=8, null = True, blank=True, default=0)
    created_by = models.ForeignKey(User, related_name= 'user', on_delete=models.CASCADE, null=True)

