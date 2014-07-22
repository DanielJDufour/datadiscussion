from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
  template = loader.get_template('dataportal/index.html')
  return HttpResponse(template.render())

def view(request):
  return HttpResponse("Hello.  You're at the view data page.")

def submit(request):
  return HttpResponse("Hello.  You're at the submit data page.")
