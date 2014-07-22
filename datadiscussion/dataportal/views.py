from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from dataportal.models import SiteInfo


def index(request):
    return render(request, 'dataportal/index.html', {'topic': 'hyrule'})

def view(request):
  return HttpResponse("Hello.  You're at the view data page.")

def submit(request):
  return HttpResponse("Hello.  You're at the submit data page.")
