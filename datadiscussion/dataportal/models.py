from django.db import models
from django.db.models.signals import post_save, m2m_changed

class SiteInfo(models.Model):
  topic = models.CharField(max_length=200, default='Add Your Topic Here!')
  domain = models.URLField(default='AddYourDomain!!', null=True)
  bg = models.ImageField("Background Pic", upload_to="dataportal/static/dataportal/images/", blank=True, null=True)
  ico = models.ImageField("Logo Ico", upload_to="images/", blank=True, null=True)

class Dataset(models.Model):
  title_en = models.CharField(max_length=200, verbose_name="title", blank=True, null=True)
  source_en = models.CharField(max_length=200, verbose_name="source", blank=True, null=True)
  hyperlink_en = models.URLField(max_length=200, verbose_name="hyperlink", default='http://', blank=True, null=True)
  locations_en = models.ManyToManyField("Location", verbose_name="location", blank=True)
  locations_en_string = models.CharField(max_length=200, default="", null=True, blank=True)
  themes_en = models.ManyToManyField('Theme', verbose_name="theme", blank=True)
  themes_en_string = models.CharField(max_length=200, default="", null=True, blank=True)
  formats_en = models.ManyToManyField('DatasetFormat', verbose_name="format", blank=True)
  formats_en_string = models.CharField(max_length=200, default="", null=True, blank=True)
  frequency_en = models.CharField(max_length=200, verbose_name="frequency", blank=True, null=True)
  strengths_en = models.TextField(verbose_name="strengths", blank=True, null=True)
  weaknesses_en = models.TextField(verbose_name="weaknesses", blank=True, null=True)
  downloadable = models.NullBooleanField(verbose_name="downloadable", blank=True, null=True)
  last_updated = models.DateTimeField(verbose_name="last_updated", blank=True, null=True)

  def get_model_fields(self):
    return self._meta.fields

  def __str__(self):
    return self.title_en


class Location(models.Model):
  title = models.CharField(max_length=200, blank=True, null=True)
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']

class Theme(models.Model):
  title = models.CharField(max_length=200, blank=True, null=True)
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']

class DatasetFormat(models.Model):
  title = models.CharField(max_length=200, blank=True, null=True)
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']

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

def calculateLocations(sender, instance, **kwargs):
  instance.save()
  instance.locations_en_string = ", ".join([location.title for location in instance.locations_en.all()])
  instance.save()

def calculateThemes(sender, instance, **kwargs):
  instance.save()
  instance.themes_en_string = ", ".join([theme.title for theme in instance.themes_en.all()])
  instance.save()

def calculateFormats(sender, instance, **kwargs):
  instance.save()
  instance.formats_en_string = ", ".join([datasetFormat.title for datasetFormat in instance.formats_en.all()])
  instance.save()

m2m_changed.connect(calculateLocations, sender=Dataset.locations_en.through)
m2m_changed.connect(calculateThemes, sender=Dataset.themes_en.through)
m2m_changed.connect(calculateFormats, sender=Dataset.formats_en.through)
