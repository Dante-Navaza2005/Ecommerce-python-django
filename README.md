# Ecommerce python django

# **INITIALIZING**

 Repository containin the files for the ecomerce website replica of reserva

Create a virtual enviroment in vscode

Start by installing django:

```
pip install django
```

Whithout exiting the comand prompt, create the necessary folders with:

```
django-admin startproject ecommerce
```

![1711736113464](image/README/1711736113464.png)

Acess the manage.py file: 

```
cd ecommerce
```

A django site is composed of many "apps" (sub-sites) that contain major features of the main site. Ex: a blog would be a separate "app" from a online store as they have significantly different features

Run: python manage.py startapp store
This will create a new folder that will contain the features related to the online store

![1711736776968](image/README/1711736776968.png)

to run the app locally: python manage.py runserver

IN THE ECOMMERCE FILE -----------

The manage.py file will manage and load all the configurations  (located inside the settings.py file) of the website

The __ init __.py file only establishes the ecommerce folder as a module/project folder so the manage.py file can pull data from there

The wsgi.py and asgi.pi files  will only be used in the final deployment fase

The urls.puy file configures the url of the website and what content it will load based on the url

Lastly the settings.py file is where we will configure the settings of the website such as criptografy, debuging mode, installed apps etc

![1711738045429](image/README/1711738045429.png)

IN THE STORE APP FILE-----

The migration folder will store the modifications done in the databases

The __ init __.py file serves the same purpose as the ecommerce file

The admin.py file will contain what will appear in the admin page of the website

The models.py file will contain the  content necessary for the creation of the products

The apps.py file delcares the name of the app to be added in the main configuration

The tests.py file is useful for performing tests and experiment features

The views.py file will contains what will appear in each url mentioned in the urls.py file

---

# Code Start (first page)

In the urls.py file we added the include() function in the imports to use the urls from other apps

```python
from django.urls import path, include #? Added the include function to use the urls from the store app
```

We will create our first url path for the main online store which will acess the links on the store urls file:

```python
path('', include('store.urls')), #? all the links from the store app will be loaded on the  root url (as we will only use one app, 'store')
```

Next we will create the urls.py file in the store folder so it can be acessed. Afterwards we will add the link of the homepage

In order to do that, we will first add a homepage() function to the views.py file as it is responsible for what happens in each url.

```python
def homepage():
    pass
```

Now we will create the homepage url:

```python
from django.urls import path
from .views import * #? Importing everything from the views folder in the same directory

urlpatterns = [
    path('', homepage, name="homepage"), #? first parameter is the url, second is what function will be runned at the url, and the third is the internal name of the link used to reference the link regardless of its url domain
]
```

When you enter a website link you are doing a **request** to that website.  Said requests usally have two formats:

* GET: Getting a desired information
* POST:  Sending a determined information to the website

This will be seen in the homepage() function, that will recieve a request as its parameter so it can return the html file of the homepage template, which will be created inside a templates folder on the store file  that django will automatically search for.

![1711742186159](image/README/1711742186159.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    Hello World!
</body>
</html>
```

Now we will edit the homepage function in the store's views.py file to recieve the request of returning said html file.

```python
def homepage(request): #? the first parameter always has to be a request
    return render(request, 'homepage.html') #? returns the homepage
```

Testing (remember to always be inside the ecommerce folder in the cmd prompt):

```
cd ecommerce
```

```
python manage.py runserver
```

![1711742566384](image/README/1711742566384.png)
