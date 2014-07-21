from django.db import models

class Dataset(models.Model):
  title_en = models.CharField(max_length=200)
  source_en = models.CharField(max_length=200)
  hyperlink_en = models.URLField(max_length=200)
  theme_en = models.CharField(max_length=200)
  type_en = models.CharField(max_length=200)
  frequency = models.CharField(max_length=200)
  strengths_en = models.CharField(max_length=200)
  weaknesses_en = models.CharField(max_length=200)
  downloadable = models.NullBooleanField()
  last_updated = models.DateTimeField()
