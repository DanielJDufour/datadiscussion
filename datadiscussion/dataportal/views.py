from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello.  You're at the data discussion index.")

def view(request):
  return HttpResponse("Hello.  You're at the view data page.")

def submit(request):
  return HttpResponse("Hello.  You're at the submit data page.")
