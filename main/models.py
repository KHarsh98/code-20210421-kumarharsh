from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    gender = models.CharField(max_length=100, default="", editable=False)
    bmi = models.FloatField()
    bmi_cat = models.CharField(max_length=100)
    health_risk = models.CharField(max_length=100)
