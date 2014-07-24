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

from dataportal.models import SiteInfo
from django.contrib.auth import login


def test(request):
    return render(request, 'dataportal/test.html')


def index(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/index.html', {'topic': topic})

def view(request):
  return HttpResponse("Hello.  You're at the view data page.")

def submit(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/submit.html', {'topic': topic})




def register(request):
    if request.method == "POST":
        User.objects.create(username='username', email='email', password='password')
    return render(request, 'dataportal/register.html') 
