# Creating first page

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

![1712083851705](image/creating_first_page/1712083851705.png)

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

![1712083868573](image/creating_first_page/1712083868573.png)
