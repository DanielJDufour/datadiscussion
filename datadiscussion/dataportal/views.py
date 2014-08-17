

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from dataportal.models import SiteInfo, Dataset, Theme, DatasetFormat
from django.contrib.auth import login
import json
from django.core import serializers

def test(request):
    return render(request, 'dataportal/test.html')


def index(request):
    topic = SiteInfo.objects.all()[0].topic
    domain = SiteInfo.objects.all()[0].domain
    return render(request, 'dataportal/index.html', {'topic': topic, 'domain': domain})

def view_data(request):
  topic = SiteInfo.objects.all()[0].topic
  domain = SiteInfo.objects.all()[0].domain
  datasets = Dataset.objects.all()
  json = serializers.serialize('json', datasets)
  json = json.replace('&',"X")
  fields = Dataset.get_model_fields(Dataset.objects.all()[0])
  fields_filterable = Dataset.get_filterable_fields(Dataset.objects.all()[0])
  locations = Dataset.objects.values_list('location_in_english').distinct()
  themes = [theme.encode("utf8") for theme in Theme.objects.values_list('theme', flat=True).distinct()]
  dataset_formats = [dataset_format.encode("utf8") for dataset_format in DatasetFormat.objects.values_list('dataset_format', flat=True).distinct()]
  return render(request, 'dataportal/view.html', {'topic': topic, 'domain': domain, "fields": fields, 'datasets': datasets, 'locations': locations, 'themes': themes, 'dataset_formats': dataset_formats, 'json': json, 'fields_filterable': fields_filterable})

def submit_data(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/submit.html', {'topic': topic})

def about(request):
    return HttpResponse("Hello. You're at the about page.")


def register(request):
    if request.method == "POST":
        User.objects.create(username='username', email='email', password='password')
    return render(request, 'dataportal/register.html') 
