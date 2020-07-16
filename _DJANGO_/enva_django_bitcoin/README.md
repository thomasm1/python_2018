### ENV: bitcoin 
## Miscellaneous Commands
#### django-admin startproject enva_django_bitcoin
#### python manage.py runserver
#### pip install mysqlclient #[if error: pip install --only-binary :all: mysqlclient ]
	[in settings.py]
	DATABASES = { 
	'default': { 
	'ENGINE': django.db.backends.mysql',
	'NAME': 'djangoproject',
	'USER': 'root',
	'PASSWORD': 'xyz',
	'HOST': 'localhost',
	'PORT': ''
#### localhost:8000/admin # DB
#### python manage.py migrate
#### python manage.py startapps pages
#### python manage.py makemigrations 
#### python manage.py migrate

django superuser enva_django_bitcoin
"thomas", "!!"