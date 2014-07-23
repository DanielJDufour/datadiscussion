from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from dataportal.models import SiteInfo


def index(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/index.html', {'topic': topic})

def view(request):
  return HttpResponse("Hello.  You're at the view data page.")

def submit(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/submit.html', {'topic': topic})
