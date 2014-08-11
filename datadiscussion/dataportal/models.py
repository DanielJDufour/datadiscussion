

from django.db import models

class SiteInfo(models.Model):
  topic = models.CharField(max_length=200)
  domain = models.URLField(default='AddYourDomain!!', null=True)
  bg = models.ImageField("Background Pic", upload_to="dataportal/static/dataportal/images/", blank=True, null=True)
  ico = models.ImageField("Logo Ico", upload_to="images/", blank=True, null=True)

class Dataset(models.Model):
  title_in_english = models.CharField(max_length=200)
  source_in_english = models.CharField(max_length=200)
  hyperlink_in_english = models.URLField(max_length=200, default='http://')
  location_in_english = models.CharField(max_length=200)
  themes_in_english = models.ManyToManyField('Theme')
  formats_in_english = models.ManyToManyField('DatasetFormat')
  frequency_in_english = models.CharField(max_length=200)
  strengths_in_english = models.TextField()
  weaknesses_in_english = models.TextField()
  downloadable = models.NullBooleanField()
  last_updated = models.DateTimeField()
  def get_model_fields(self):
    return self._meta.fields
  def __str__(self):
    return self.title_in_english  

class Theme(models.Model):
  theme = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.theme
  class Meta:
    ordering = ['theme']

class DatasetFormat(models.Model):
  dataset_format = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.dataset_format
  class Meta:
    ordering = ['dataset_format']

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
