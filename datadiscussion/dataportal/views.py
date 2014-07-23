from dataportal.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext





from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from dataportal.models import UserProfile, UserForm, UserProfileForm, SiteInfo

def test(request):
    return render(request, 'dataportal/submit.html')


def index(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/index.html', {'topic': topic})

def view(request):
  return HttpResponse("Hello.  You're at the view data page.")

def submit(request):
    topic = SiteInfo.objects.all()[0].topic
    return render(request, 'dataportal/submit.html', {'topic': topic})







@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'dataportal/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'dataportal/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
