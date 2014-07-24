# from http://stackoverflow.com/questions/11287485/taking-user-input-to-create-users-in-django

from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
