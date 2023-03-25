
# Comandos

```bash

python-m venv venv
pyton venv/bin/activate
pip install -r requirements.txt

pip install django

python-admin startproject mysite
python manage.py startapp myapp
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate
```

### Settings

```
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'rest_framework',
  'corsheaders',
  'almacen',
]
```

### Model

```python
from django.db import models

class MyModel(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

### Model admin

```
from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description', 'created_at', 'updated_at')

admin.site.register(MyModel)
```

### Resources

* https://pypi.org/project/django-cors-headers/
* https://github.com/12aptor/django-repaso-g11/