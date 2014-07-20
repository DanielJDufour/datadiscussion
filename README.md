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
libpq-dev and postgresql-server-dev-X.Y are needed in order to install psycopg2 later
```
sudo apt-get install -y postgresql libpq-dev postgresql-server-dev-all
```

###Install Pyton
It might already be installed.  If that's so, no worries.
```
sudo apt-get -y install python python-dev;
```

####Download Pip
Pip will be used to make the django code importable into Python
```
sudo apt-get -y install python-pip
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

####Make Django Code Importable
Make Django code importable into Python with the following
```
sudo pip install -e ~/django-trunk/
```
