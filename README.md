###Data Discussion Installation Guide

####Update
```
sudo apt-get update
```

####Install Packages That We'll Use Later
```
sudo apt-get install -y curl vim git
```

####Install PostgreSQL
```
sudo apt-get install -y postgresql libpq-dev postgresql-server-dev-X.Y
```

###Install Pyton
It might already be installed.  If that's so, no worries.
```
sudo apt-get install python python-dev;
```

###Install Psycopg
Psycopg is a PostgreSQL database adapater for Python
```
sudo pip install psycopg2;
```


####Download Django
The following code will download the django code into the current user's home directory. 
```
git clone http://github.com/django/django.git ~/django-trunk
```

####Download Pip
Pip will be used to make the django code importable into Python
```
sudo apt-get -y install python-pip
```

####Make Django Code Importable
Make Django code importable into Python with the following
```
sudo pip install -e ~/django-trunk/
```
