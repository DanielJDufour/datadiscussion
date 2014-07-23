from django.db import models, forms
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class SiteInfo(models.Model):
  topic = models.CharField(max_length=200)
  bg = models.ImageField("Background Pic", upload_to="dataportal/static/dataportal/images/", blank=True, null=True)
  ico = models.ImageField("Logo Ico", upload_to="images/", blank=True, null=True)

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
