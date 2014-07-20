Installation Guide

```
sudo apt-get update;
sudo apt-get install -y curl vim git;
sudo apt-get install -y postgresql;
```

###Install Pyton
It might already be installed.  If that's so, no worries.
```
sudo apt-get install python;
```

####Download Django
```
git clone http://github.com/django/django.git ~/django-trunk
```

####Download Pip
Pip will be used to make the django code importable into Python
```
sudo apt-get -y install python-pip
```





```
sudo -u postgres createuser --pwprompt --createdb --login --echo datadiscussion;
```

