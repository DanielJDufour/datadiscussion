###Data Discussion Installation Guide

####Update
```
sudo apt-get update
```

####Install Required Packages
```
sudo apt-get install -y curl vim git postgresql libpq-dev postgresql-server-dev-all python python-dev python-pip
```
curl: is used to download form th e
python-pip: is used to install python packages

####Install PostgreSQL
libpq-dev and postgresql-server-dev-X.Y are needed in order to install psycopg2 later

####Create Database
You will now create the databse that the Django app will use.  The database is called datadiscussion.
```
sudo -u postgres createdb datadiscussion;
```

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

####Download This Repo
```
git clone http://github.com/danieljdufour/datadiscussion.git ~/datadiscussion
```

####Install Tastypie and its dependencies
sudo pip install python-mimeparse
sudo pip install python-dateutil
sudo git clone https://github.com/toastdriven/django-tastypie.git ~/django-tastypie
sudo pip install ~/django-tastypie
ln -s ~/django-tastypie/ ~/datadiscussion/datadiscussion/tastypie
sudo pip install -r ~/django-tastypie/requirements.txt

####Create Database (db) Tables
The following command creates the tables needed by the INSTALLED_APPS found in ~/datadiscussion/datadiscussion/datadiscussion/settings.py.  ```sudo -u postgres``` makes it so you run the command as the postgres user, which has a role to access the database. 
```
sudo python ~/datadiscussion/datadiscussion/manage.py makemigrations
sudo -u postgres python ~/datadiscussion/datadiscussion/manage.py migrate
```

####Run the Development Server
```
sudo -u postgres python ~/datadiscussion/datadiscussion/manage.py runserver
```

####Create Admin User
The following command will prompt you for a username and email address.
Enter ```admin``` as username and enter your email address.
And enter your password twice.
```
sudo -u postgres python ~/datadiscussion/datadiscussion/manage.py createsuperuser;
```

####Add Site Topic and Background Image
