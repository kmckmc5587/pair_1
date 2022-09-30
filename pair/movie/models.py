from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)