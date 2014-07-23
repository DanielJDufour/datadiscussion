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

####Create Database
You will now create the databse that the Django app will use.  The database is called datadiscussion.
```
sudo -u postgres createdb datadiscussion;
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

####Download This Repo
```
git clone http://github.com/danieljdufour/datadiscussion.git ~/datadiscussion
```

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
