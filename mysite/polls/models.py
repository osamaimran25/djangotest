from django.db import models

# Create your models here.
class Sample(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=80)