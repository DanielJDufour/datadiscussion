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
from dataportal.models import SiteInfo, Dataset
from django.contrib.auth import login


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
  fields = Dataset.get_model_fields(Dataset.objects.all()[0])
  return render(request, 'dataportal/view.html', {'topic': topic, 'domain': domain, "fields": fields, "datasets": datasets})

def submit_data(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/submit.html', {'topic': topic})

def about(request):
    return HttpResponse("Hello. You're at the about page.")


def register(request):
    if request.method == "POST":
        User.objects.create(username='username', email='email', password='password')
    return render(request, 'dataportal/register.html') 
