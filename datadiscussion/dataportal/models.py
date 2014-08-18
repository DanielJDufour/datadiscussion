

from django.db import models

class SiteInfo(models.Model):
  topic = models.CharField(max_length=200)
  domain = models.URLField(default='AddYourDomain!!', null=True)
  bg = models.ImageField("Background Pic", upload_to="dataportal/static/dataportal/images/", blank=True, null=True)
  ico = models.ImageField("Logo Ico", upload_to="images/", blank=True, null=True)



class Dataset(models.Model):
  title_in_english = models.CharField(max_length=200, verbose_name="title")
  source_in_english = models.CharField(max_length=200, verbose_name="source")
  hyperlink_in_english = models.URLField(max_length=200, verbose_name="hyperlink", default='http://')
  locations_in_english = models.ManyToManyField("Location", verbose_name="location")
  locations_in_english_string = models.CharField(max_length=200, default='', null=True, blank=True)
  themes_in_english = models.ManyToManyField('Theme', verbose_name="theme")
  formats_in_english = models.ManyToManyField('DatasetFormat', verbose_name="format")
  frequency_in_english = models.CharField(max_length=200, verbose_name="frequency")
  strengths_in_english = models.TextField(verbose_name="strengths")
  weaknesses_in_english = models.TextField(verbose_name="weaknesses")
  downloadable = models.NullBooleanField(verbose_name="downloadable")
  last_updated = models.DateTimeField(verbose_name="last_updated")

  def convertListToString(self, elements):
    converted = ""
    firstElement = True
    for element in elements:
      if firstElement:
        converted += element.title
        firstElement = False
      else:
        converted += ", " + element.title

    return converted

  def save(self):
    self.locations_in_english_string = self.convertListToString(self.locations_in_english.all())
    self.themes_in_english_string = self.convertListToString(self.themes_in_english.all())
    self.formats_in_english_string = self.convertListToString(self.formats_in_english.all())
    super(Dataset, self).save()

  def get_model_fields(self):
    return self._meta.fields

  def get_filterable_fields(self):
    fields_all = self._meta.fields
    fields_filterable = []
    for field in fields_all:
      print field.name 
      if isinstance(field,models.CharField):
        print "isinstance is true!"
        fields_filterable.append(field)
    print "fields_all is "
    print fields_all
    print "returning fields_filterable of "
    print fields_filterable
    return fields_filterable

  def __str__(self):
    return self.title_in_english  


class Location(models.Model):
  title = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']

class Theme(models.Model):
  title = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']

class DatasetFormat(models.Model):
  title = models.CharField(max_length=200, null=True)
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
