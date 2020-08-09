from django.db import models

# Create your models here.

class Recipes(models.Model):
    ingredients = models.CharField(max_length = 10000000000000000)
    method = models.CharField(max_length = 10000000000000000)
    name = models.CharField(max_length= 64)
    
