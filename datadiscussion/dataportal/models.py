from django.db import models

class DataSet(models.Model):
  title = models.CharField(max_length=200)
  source = models.CharField(max_length=200)
  strengths = models.CharField(max_length=200)
  weaknesses = models.CharField(max_length=200)
