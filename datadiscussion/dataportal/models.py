from django.db import models

class Dataset(models.Model):
  title_in_english = models.CharField(max_length=200)
  source_in_english = models.CharField(max_length=200)
  hyperlink_in_english = models.URLField(max_length=200)
  location_in_english = models.CharField(max_length=200)
  location_in_english = models.URLField(max_length=200)
  theme_in_english = models.CharField(max_length=200)
  format_in_english = models.CharField(max_length=200)
  frequency_in_english = models.TextField()
  strengths_in_english = models.TextField()
  weaknesses_in_english = models.CharField(max_length=200)
  downloadable = models.NullBooleanField()
  last_updated = models.DateTimeField()
  def __str__(self):
    return self.title_en  

class Twitter(models.Model):
  dataset = models.ForeignKey(Dataset)
  handle = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  bio = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  website = models.CharField(max_length=200)
  tweets = models.IntegerField(default=0)
  following = models.IntegerField(default=0)
  followers = models.IntegerField(default=0)

class Facebook(models.Model):
  dataset = models.ForeignKey(Dataset)
  likes = models.IntegerField(default=0)
  talking = models.IntegerField(default=0)
  
class GIS(models.Model):
  dataset = models.ForeignKey(Dataset)
  imagery_date = models.DateField()
  resolution = models.IntegerField(default=0)
